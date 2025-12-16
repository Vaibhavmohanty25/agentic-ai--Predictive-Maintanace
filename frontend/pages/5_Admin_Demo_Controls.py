import streamlit as st
import requests

st.set_page_config(page_title="Demo Controls", page_icon="🧪", layout="wide")

st.title("🧪 Demo Mode Controls")
st.markdown("Control panel for managing demo behavior during presentations")

BACKEND_URL = "http://localhost:8000"


def get_current_mode():
    try:
        res = requests.get(f"{BACKEND_URL}/sensors/live", timeout=5)
        data = res.json().get("data", [])
        if data:
            return data[0].get("mode", "normal")
        return "normal"
    except:
        return "unknown"


def set_mode(mode):
    try:
        res = requests.post(f"{BACKEND_URL}/demo/mode/{mode}", timeout=5)
        return res.json()
    except:
        return {"error": "Backend unreachable"}


def reset_demo():
    try:
        res = requests.post(f"{BACKEND_URL}/demo/reset", timeout=5)
        return res.json()
    except:
        return {"error": "Backend unreachable"}


st.markdown("---")

# Current Mode Display
current_mode = get_current_mode()

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 🎮 Current Mode")
    
    if current_mode == "failure":
        st.markdown("""
        <div style="background: linear-gradient(135deg, #dc3545 0%, #c82333 100%);
                    border-radius: 15px; padding: 30px; text-align: center; color: white;">
            <h1 style="margin: 0;">⚠️</h1>
            <h2 style="margin: 10px 0 0 0;">FAILURE MODE</h2>
            <p style="opacity: 0.9;">Simulating anomalies</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
                    border-radius: 15px; padding: 30px; text-align: center; color: white;">
            <h1 style="margin: 0;">✅</h1>
            <h2 style="margin: 10px 0 0 0;">NORMAL MODE</h2>
            <p style="opacity: 0.9;">Standard operation</p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("### ⚙️ Mode Configuration")
    
    st.markdown("""
    | Mode | Description | Use Case |
    |------|-------------|----------|
    | **Normal** | All sensors report healthy values | Show baseline monitoring |
    | **Failure** | MACHINE_2 reports critical anomalies | Demonstrate diagnosis + scheduling |
    """)
    
    st.markdown("---")
    
    mode_col1, mode_col2 = st.columns(2)
    
    with mode_col1:
        if st.button("🟢 Set NORMAL Mode", use_container_width=True, 
                     disabled=(current_mode == "normal")):
            response = set_mode("normal")
            if "error" in response:
                st.error(response["error"])
            else:
                st.success("✅ Switched to NORMAL mode!")
                st.rerun()
    
    with mode_col2:
        if st.button("🔴 Set FAILURE Mode", use_container_width=True,
                     disabled=(current_mode == "failure"), type="primary"):
            response = set_mode("failure")
            if "error" in response:
                st.error(response["error"])
            else:
                st.success("⚠️ Switched to FAILURE mode!")
                st.balloons()
                st.rerun()

st.markdown("---")

# Reset Section
st.markdown("### 🔄 Reset Demo Environment")

col_a, col_b = st.columns([2, 1])

with col_a:
    st.markdown("""
    **Reset will:**
    - Clear all scheduled jobs from database
    - Clear all feedback records
    - Reset system to clean state
    
    ⚠️ **Note:** This action cannot be undone.
    """)

with col_b:
    if st.button("🗑️ Reset All Demo Data", use_container_width=True):
        with st.spinner("Resetting demo environment..."):
            response = reset_demo()
        
        if "error" in response:
            st.error(f"Failed: {response['error']}")
        else:
            st.success("✅ Demo environment reset successfully!")
            st.balloons()

st.markdown("---")

# Demo Script
st.markdown("### 📝 Suggested Demo Script")

with st.expander("Click to view demo walkthrough", expanded=False):
    st.markdown("""
    #### 1️⃣ Start in Normal Mode
    - Show **Live Sensors** page with healthy readings
    - Demonstrate all 4 machines showing green status
    - Point out low risk scores in **Diagnosis Console**
    
    #### 2️⃣ Switch to Failure Mode
    - Come back here and click **Set FAILURE Mode**
    - Navigate to **Live Sensors** - notice MACHINE_2 shows critical values
    
    #### 3️⃣ Diagnose the Problem
    - Go to **Diagnosis Console**
    - Select MACHINE_2
    - Show the AI-generated diagnosis and recommendations
    
    #### 4️⃣ Schedule Maintenance
    - Navigate to **Service Scheduling**
    - Select MACHINE_2
    - Click **Schedule Maintenance**
    - Show the autonomous job creation
    
    #### 5️⃣ Show Business Impact
    - Go to **Insights Dashboard**
    - Display the updated KPIs
    - Highlight the agent activity summary
    
    #### 6️⃣ Reset for Next Demo
    - Return here and click **Reset All Demo Data**
    """)

st.markdown("---")

# Footer
st.markdown("""
<div style="text-align: center; color: #888; padding: 20px;">
    <p>🔧 Agentic AI – Predictive Maintenance Demo</p>
    <p>Built for hackathon presentations | Fully deterministic | Works offline</p>
</div>
""", unsafe_allow_html=True)
