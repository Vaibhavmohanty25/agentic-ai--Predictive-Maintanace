import streamlit as st
import requests

st.set_page_config(page_title="Insights Dashboard", page_icon="📊", layout="wide")

st.title("📊 Manufacturing Insights Dashboard")
st.markdown("Real-time KPIs and business intelligence from agent activity")

BACKEND_URL = "http://localhost:8000"


def fetch_insights():
    try:
        res = requests.get(f"{BACKEND_URL}/insights/summary", timeout=5)
        return res.json()
    except:
        return {"error": "Cannot reach backend"}


st.markdown("---")

insights = fetch_insights()

if "error" in insights:
    st.error(f"⚠️ {insights['error']}")
else:
    # Main KPI Cards
    st.markdown("### 🎯 Key Performance Indicators")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    border-radius: 15px; padding: 25px; text-align: center; color: white;">
            <h1 style="margin: 0; font-size: 3rem;">{}</h1>
            <p style="margin: 5px 0 0 0; opacity: 0.9;">Total Assets</p>
        </div>
        """.format(insights["total_assets"]), unsafe_allow_html=True)
    
    with col2:
        high_risk = insights["high_risk_assets"]
        bg_color = "#dc3545" if high_risk > 0 else "#28a745"
        st.markdown(f"""
        <div style="background: {bg_color}; border-radius: 15px; 
                    padding: 25px; text-align: center; color: white;">
            <h1 style="margin: 0; font-size: 3rem;">{high_risk}</h1>
            <p style="margin: 5px 0 0 0; opacity: 0.9;">High-Risk Assets</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
                    border-radius: 15px; padding: 25px; text-align: center; color: white;">
            <h1 style="margin: 0; font-size: 3rem;">{}</h1>
            <p style="margin: 5px 0 0 0; opacity: 0.9;">Jobs Scheduled</p>
        </div>
        """.format(insights["jobs_scheduled"]), unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                    border-radius: 15px; padding: 25px; text-align: center; color: white;">
            <h1 style="margin: 0; font-size: 3rem;">{}</h1>
            <p style="margin: 5px 0 0 0; opacity: 0.9;">Jobs Completed</p>
        </div>
        """.format(insights["jobs_completed"]), unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Failure Rate Section
    col_left, col_right = st.columns([1, 2])
    
    with col_left:
        st.markdown("### 📈 Completion Rate")
        
        failure_rate = insights['failure_rate']
        completion_pct = failure_rate * 100
        
        # Gauge-like display
        if completion_pct >= 80:
            color = "#28a745"
            status = "Excellent"
        elif completion_pct >= 50:
            color = "#ffc107"
            status = "Good"
        else:
            color = "#dc3545"
            status = "Needs Attention"
        
        st.markdown(f"""
        <div style="background: #f8f9fa; border-radius: 15px; padding: 30px; text-align: center;">
            <h1 style="margin: 0; font-size: 4rem; color: {color};">{completion_pct:.0f}%</h1>
            <p style="margin: 10px 0 0 0; font-size: 1.2rem; color: #666;">{status}</p>
            <div style="background: #e9ecef; border-radius: 10px; height: 20px; margin-top: 15px;">
                <div style="background: {color}; width: {min(completion_pct, 100)}%; 
                            height: 100%; border-radius: 10px;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_right:
        st.markdown("### 🤖 Agent Activity Summary")
        
        st.markdown(f"""
        | Metric | Value | Status |
        |--------|-------|--------|
        | **Assets Monitored** | {insights['total_assets']} | ✅ Active |
        | **Risk Assessments** | Real-time | ✅ Running |
        | **Diagnoses Performed** | On-demand | ✅ Ready |
        | **Jobs in Pipeline** | {insights['jobs_scheduled']} | {"⚠️ Pending" if insights['jobs_scheduled'] > insights['jobs_completed'] else "✅ Clear"} |
        | **Completion Rate** | {completion_pct:.0f}% | {"✅ Good" if completion_pct >= 50 else "⚠️ Low"} |
        """)
    
    st.markdown("---")
    
    # System Status
    st.markdown("### 🔄 System Status")
    
    col_a, col_b, col_c, col_d, col_e = st.columns(5)
    
    agents = [
        ("📡", "Sensor Agent", "Active"),
        ("⚠️", "Risk Agent", "Active"),
        ("🩺", "Diagnosis Agent", "Active"),
        ("📅", "Scheduler Agent", "Active"),
        ("📊", "Insights Agent", "Active")
    ]
    
    for col, (icon, name, status) in zip([col_a, col_b, col_c, col_d, col_e], agents):
        with col:
            st.markdown(f"""
            <div style="background: #d4edda; border-radius: 10px; padding: 15px; text-align: center;">
                <h2 style="margin: 0;">{icon}</h2>
                <p style="margin: 5px 0; font-weight: bold;">{name}</p>
                <p style="margin: 0; color: #28a745; font-size: 0.9rem;">● {status}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.info("💡 **Tip:** Schedule more maintenance jobs to see metrics update in real-time!")
