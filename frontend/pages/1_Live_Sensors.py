import streamlit as st
import requests
import pandas as pd
import time

st.set_page_config(page_title="Live Sensors", page_icon="📡", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .sensor-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
    }
    .status-normal { color: #28a745; font-weight: bold; }
    .status-warning { color: #ffc107; font-weight: bold; }
    .status-critical { color: #dc3545; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.title("📡 Live Sensor Dashboard")
st.markdown("Real-time monitoring of manufacturing asset health")

BACKEND_URL = "http://localhost:8000"


def fetch_sensors():
    try:
        res = requests.get(f"{BACKEND_URL}/sensors/live", timeout=5)
        return res.json().get("data", [])
    except:
        return []


def get_status_color(temp, vibration):
    if temp > 85 or vibration > 3:
        return "🔴", "CRITICAL"
    elif temp > 70 or vibration > 2:
        return "🟡", "WARNING"
    return "🟢", "NORMAL"


st.markdown("---")

# Controls
col1, col2, col3 = st.columns([1, 1, 2])
with col1:
    if st.button("🔄 Refresh Data", use_container_width=True):
        st.rerun()
with col2:
    auto_refresh = st.checkbox("Auto-refresh (5s)")

# Fetch data
data = fetch_sensors()

if not data:
    st.error("⚠️ No sensor data available. Please ensure the backend is running.")
    st.code("uvicorn app.main:app --reload --port 8000", language="bash")
else:
    st.success(f"✅ Connected | {len(data)} assets monitored | Mode: **{data[0].get('mode', 'unknown').upper()}**")
    
    st.markdown("---")
    st.markdown("### 📊 Asset Overview")
    
    # Display as cards
    cols = st.columns(len(data))
    
    for i, sensor in enumerate(data):
        with cols[i]:
            icon, status = get_status_color(sensor['temperature'], sensor['vibration'])
            
            st.markdown(f"""
            <div style="background: white; border-radius: 15px; padding: 20px; 
                        box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center;">
                <h3>{icon} {sensor['asset_id']}</h3>
                <p style="color: gray;">Status: <strong>{status}</strong></p>
            </div>
            """, unsafe_allow_html=True)
            
            st.metric("🌡️ Temperature", f"{sensor['temperature']}°C")
            st.metric("📳 Vibration", f"{sensor['vibration']} mm/s")
            st.metric("💨 Pressure", f"{sensor['pressure']} PSI")
            st.metric("⚙️ RPM", f"{sensor['rpm']}")
    
    st.markdown("---")
    st.markdown("### 📋 Raw Data Table")
    
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp']).dt.strftime('%H:%M:%S')
    st.dataframe(df, use_container_width=True, hide_index=True)

# Auto refresh
if auto_refresh:
    time.sleep(5)
    st.rerun()
