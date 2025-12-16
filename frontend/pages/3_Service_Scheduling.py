import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Service Scheduling", page_icon="🛠", layout="wide")

st.title("🛠 Maintenance Scheduling")
st.markdown("AI-powered autonomous maintenance job scheduling")

BACKEND_URL = "http://localhost:8000"


def get_assets():
    try:
        res = requests.get(f"{BACKEND_URL}/sensors/live", timeout=5)
        data = res.json().get("data", [])
        return [d["asset_id"] for d in data]
    except:
        return []


def analyze_asset(asset_id):
    try:
        res = requests.get(f"{BACKEND_URL}/diagnosis/{asset_id}", timeout=5)
        return res.json()
    except:
        return {"error": "Backend not reachable"}


def schedule_job(asset_id, severity):
    try:
        payload = {"asset_id": asset_id, "severity": severity}
        res = requests.post(f"{BACKEND_URL}/scheduling/job", json=payload, timeout=5)
        return res.json()
    except:
        return {"error": "Scheduling failed"}


def get_jobs():
    try:
        res = requests.get(f"{BACKEND_URL}/scheduling/jobs", timeout=5)
        return res.json()
    except:
        return []


st.markdown("---")

# Two-column layout
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 🏭 Schedule New Job")
    
    assets = get_assets()
    
    if not assets:
        st.error("No assets available.")
    else:
        selected = st.selectbox("Select Asset", assets)
        
        if selected:
            status = analyze_asset(selected)
            
            if "error" not in status:
                risk = status.get("risk", {})
                severity = risk.get("risk_level", "LOW")
                risk_score = risk.get("risk_score", 0)
                
                # Severity indicator
                severity_colors = {
                    "LOW": "🟢",
                    "MEDIUM": "🟡", 
                    "HIGH": "🟠",
                    "CRITICAL": "🔴"
                }
                
                st.markdown(f"""
                <div style="background: #f8f9fa; border-radius: 10px; padding: 15px; margin: 15px 0;">
                    <p style="margin: 0;"><strong>Detected Severity:</strong></p>
                    <h2 style="margin: 5px 0;">{severity_colors.get(severity, "⚪")} {severity}</h2>
                    <p style="margin: 0; color: #666;">Risk Score: {risk_score:.0%}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Scheduling info
                schedule_times = {
                    "CRITICAL": "⚡ Within 1 hour",
                    "HIGH": "📅 Within 8 hours",
                    "MEDIUM": "📆 Within 2 days",
                    "LOW": "🗓️ Within 5 days"
                }
                st.info(f"**Scheduled Time:** {schedule_times.get(severity, 'TBD')}")
                
                if st.button("📅 Schedule Maintenance", use_container_width=True, type="primary"):
                    with st.spinner("Scheduling maintenance job..."):
                        result = schedule_job(selected, severity)
                    
                    if "error" in result:
                        st.error(f"Failed: {result['error']}")
                    else:
                        st.success("✅ Maintenance Scheduled!")
                        st.balloons()
                        
                        st.markdown(f"""
                        **Job ID:** `{result.get('job_id', 'N/A')[:8]}...`  
                        **Technician:** {result.get('technician', 'N/A')}  
                        **Scheduled:** {result.get('scheduled_time', 'N/A')[:19]}
                        """)

with col2:
    st.markdown("### 📋 Scheduled Jobs")
    
    jobs = get_jobs()
    
    if not jobs:
        st.info("No jobs scheduled yet. Schedule a maintenance job from the left panel.")
    else:
        # Convert to DataFrame for better display
        df = pd.DataFrame(jobs)
        
        # Status badges
        def status_badge(status):
            colors = {
                "SCHEDULED": "🔵",
                "COMPLETED": "✅",
                "FAILED": "❌",
                "IN_PROGRESS": "🔄"
            }
            return f"{colors.get(status, '⚪')} {status}"
        
        if 'status' in df.columns:
            df['status'] = df['status'].apply(status_badge)
        
        if 'scheduled_time' in df.columns:
            df['scheduled_time'] = pd.to_datetime(df['scheduled_time']).dt.strftime('%Y-%m-%d %H:%M')
        
        if 'job_id' in df.columns:
            df['job_id'] = df['job_id'].str[:8] + '...'
        
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Summary stats
        st.markdown("---")
        col_a, col_b, col_c = st.columns(3)
        
        total = len(jobs)
        completed = len([j for j in jobs if j.get('status') == 'COMPLETED'])
        pending = total - completed
        
        col_a.metric("Total Jobs", total)
        col_b.metric("Completed", completed)
        col_c.metric("Pending", pending)
