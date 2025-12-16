import streamlit as st

st.set_page_config(
    page_title="Agentic AI – Predictive Maintenance",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for polished look
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        margin-top: 0;
    }
    .feature-card {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        border-left: 4px solid #667eea;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 25px;
        color: white;
        text-align: center;
    }
    .stButton>button {
        border-radius: 20px;
        padding: 10px 25px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="main-header">🔧 Agentic AI – Predictive Maintenance</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Intelligent Manufacturing Operations Platform</p>', unsafe_allow_html=True)

st.markdown("---")

# Hero Section
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### 🚀 Welcome to the Demo
    
    This AI-powered system demonstrates **autonomous predictive maintenance** 
    for manufacturing environments. Our multi-agent architecture enables:
    
    - **Real-time anomaly detection** from sensor data
    - **Intelligent failure diagnosis** with explainable AI
    - **Autonomous maintenance scheduling** based on risk levels
    - **Actionable insights** for operations teams
    """)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h2>🤖</h2>
        <h3>5 AI Agents</h3>
        <p>Working Together</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Feature Cards
st.markdown("### 🎯 System Capabilities")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    #### 📡 Sensor Monitoring
    Live streaming of temperature, vibration, 
    pressure, and RPM data from manufacturing assets.
    """)
    
with col2:
    st.markdown("""
    #### 🩺 Smart Diagnosis
    Rule-based expert system identifies probable issues
    and provides actionable recommendations.
    """)

with col3:
    st.markdown("""
    #### 📅 Auto-Scheduling
    Maintenance jobs are autonomously scheduled
    based on detected severity levels.
    """)

st.markdown("---")

# Architecture
st.markdown("### 🧠 System Architecture")
st.code("""
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   SENSORS   │───▶│  RISK ENGINE │───▶│  DIAGNOSIS  │───▶│  SCHEDULER  │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                            │                                    │
                            ▼                                    ▼
                   ┌─────────────────────────────────────────────────┐
                   │              ORCHESTRATOR (Brain)               │
                   └─────────────────────────────────────────────────┘
                                         │
                            ┌────────────┴────────────┐
                            ▼                         ▼
                   ┌─────────────┐           ┌─────────────┐
                   │  FEEDBACK   │           │  INSIGHTS   │
                   └─────────────┘           └─────────────┘
""", language="text")

st.markdown("---")

# Navigation Guide
st.markdown("### 📍 Navigation Guide")

col1, col2 = st.columns(2)

with col1:
    st.info("**1️⃣ Live Sensors** → View real-time sensor data")
    st.info("**2️⃣ Diagnosis Console** → Analyze asset health")
    st.info("**3️⃣ Service Scheduling** → Manage maintenance jobs")

with col2:
    st.info("**4️⃣ Insights Dashboard** → Business KPIs")
    st.info("**5️⃣ Demo Controls** → Switch demo modes")

st.markdown("---")

# Footer
st.markdown("""
<div style="text-align: center; color: #888; padding: 20px;">
    <p>Built for Hackathon Demo | Fully Offline | Deterministic Outputs</p>
    <p>👈 <strong>Use sidebar to navigate</strong></p>
</div>
""", unsafe_allow_html=True)
