# 🔧 Agentic AI – Predictive Maintenance System

A demo-grade, fully offline agentic AI system designed for predictive maintenance, failure diagnosis, autonomous scheduling, and manufacturing insights.

Built for hackathon environments:

* Deterministic outputs
* Works offline
* Fast to demo
* Fully explainable agents

---

# 🚀 Features

### ✅ Live Sensor Simulation

Mocked real-time sensor readings:

* Temperature
* Vibration
* Pressure
* RPM

### ✅ Risk Scoring Agent

Computes failure probability + contributing factors.

### ✅ Diagnosis Agent

Rule-based expert system provides:

* Probable issue
* Severity level
* Triggered rules
* Recommended actions

### ✅ Scheduling Agent

Autonomously assigns maintenance slots based on severity.

### ✅ Feedback Agent

Logs technician feedback and closes job tickets.

### ✅ Insights Agent

Provides KPI dashboard:

* Jobs scheduled
* Jobs completed
* Failure rate
* High-risk assets

### ✅ Demo Mode

Two simulation modes:

* **normal**
* **failure** (forces anomalies)

---

# 🧠 System Architecture

```
SENSORS → RISK ENGINE → DIAGNOSIS → SCHEDULING → FEEDBACK → INSIGHTS
                        ↑
              ORCHESTRATOR (Brain)
```

---

# 🗂 Project Structure

```
backend/
  app/
    agents/
    core/
    routes/
    tests/
  demo/
frontend/
  app.py
  pages/
requirements.txt
.env.example
```

---

# 🛠 Installation

### 1. Clone Repository

```
git clone <your-repo-url>
cd agentic-predictive-maintenance
```

### 2. Create Virtual Environment

```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

# ▶️ Running the System

### 1. Start Backend (FastAPI)

```
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 --app-dir backend/app
```

### 2. Start Frontend (Streamlit)

```
streamlit run frontend/app.py
```

---

# 🧪 Demo Mode Usage

### Switch to failure mode:

```
POST /demo/mode/failure
```

### Switch to normal mode:

```
POST /demo/mode/normal
```

### Reset demo database:

```
POST /demo/reset
```

---

# 🎯 Demo Flow (Judge-Friendly)

1. Open **Live Sensors** → show mock telemetry
2. Switch to **Failure Mode**
3. Watch risk jump to **HIGH/CRITICAL** for Machine 2
4. Open **Diagnosis Console** → explainable fault
5. Go to **Scheduling** → click "Schedule Maintenance"
6. Add technician feedback
7. Open **Insights Dashboard** → KPIs update

---

# 🎓 Tech Stack

**Backend:** FastAPI, SQLite
**Frontend:** Streamlit
**AI Logic:** Deterministic rules + explainability
**Architecture:** Multi-agent (Orchestrator + Sub-agents)

---

# 📄 License

MIT License

---

# 🤝 Contributing

Pull requests welcome!

---

# 📬 Contact

For any queries or improvements, feel free to reach out.
