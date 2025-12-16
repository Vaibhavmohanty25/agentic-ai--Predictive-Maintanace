import streamlit as st
import requests

st.set_page_config(page_title="Diagnosis Console", page_icon="🩺", layout="wide")

st.title("🩺 AI Diagnosis Console")
st.markdown("Intelligent failure analysis powered by rule-based expert system")

BACKEND_URL = "http://localhost:8000"


def get_assets():
    try:
        res = requests.get(f"{BACKEND_URL}/sensors/live", timeout=5)
        sensors = res.json().get("data", [])
        return [s["asset_id"] for s in sensors]
    except:
        return []


def get_asset_status(asset_id):
    try:
        res = requests.get(f"{BACKEND_URL}/diagnosis/{asset_id}", timeout=5)
        return res.json()
    except:
        return {"error": "Backend not reachable"}


st.markdown("---")

assets = get_assets()

if not assets:
    st.error("⚠️ No assets detected. Is backend running?")
else:
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.markdown("### 🏭 Select Asset")
        selected = st.selectbox("Choose an asset to diagnose:", assets, label_visibility="collapsed")
        
        if st.button("🔍 Run Diagnosis", use_container_width=True):
            st.rerun()

    with col2:
        if selected:
            status = get_asset_status(selected)
            
            if "error" in status:
                st.error(status["error"])
            else:
                # Risk Level Badge
                risk = status.get("risk", {})
                risk_level = risk.get("risk_level", "UNKNOWN")
                risk_score = risk.get("risk_score", 0)
                
                risk_colors = {
                    "LOW": ("🟢", "#28a745"),
                    "MEDIUM": ("🟡", "#ffc107"),
                    "HIGH": ("🟠", "#fd7e14"),
                    "CRITICAL": ("🔴", "#dc3545")
                }
                icon, color = risk_colors.get(risk_level, ("⚪", "#6c757d"))
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, {color}22 0%, {color}11 100%);
                            border-left: 5px solid {color}; border-radius: 10px;
                            padding: 20px; margin-bottom: 20px;">
                    <h2 style="margin: 0;">{icon} Risk Level: {risk_level}</h2>
                    <p style="font-size: 1.2rem; margin: 10px 0 0 0;">
                        Risk Score: <strong>{risk_score:.0%}</strong>
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
                # Three columns for details
                col_a, col_b, col_c = st.columns(3)
                
                with col_a:
                    st.markdown("#### 📊 Sensor Readings")
                    sensor = status.get("sensor", {})
                    st.metric("Temperature", f"{sensor.get('temperature', 'N/A')}°C")
                    st.metric("Vibration", f"{sensor.get('vibration', 'N/A')} mm/s")
                    st.metric("Pressure", f"{sensor.get('pressure', 'N/A')} PSI")
                    st.metric("RPM", sensor.get('rpm', 'N/A'))
                
                with col_b:
                    st.markdown("#### ⚠️ Risk Factors")
                    factors = risk.get("factors", [])
                    if factors:
                        for factor in factors:
                            st.warning(f"• {factor}")
                    else:
                        st.success("✅ No risk factors detected")
                
                with col_c:
                    st.markdown("#### 🛠️ Diagnosis")
                    diagnosis = status.get("diagnosis", {})
                    if diagnosis:
                        st.info(f"**Issue:** {diagnosis.get('probable_issue', 'N/A')}")
                        st.markdown("**Rules Triggered:**")
                        for rule in diagnosis.get("rules_triggered", []):
                            st.code(rule)
                    else:
                        st.success("✅ No issues detected")
                
                # Recommendations
                st.markdown("---")
                st.markdown("#### 💡 Recommended Actions")
                recommendations = status.get("diagnosis", {}).get("recommendations", [])
                if recommendations:
                    for i, rec in enumerate(recommendations, 1):
                        st.markdown(f"**{i}.** {rec}")
                else:
                    st.info("No immediate actions required. Continue monitoring.")
