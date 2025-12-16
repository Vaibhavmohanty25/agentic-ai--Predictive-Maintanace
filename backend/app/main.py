from fastapi import FastAPI
from app.routes import sensors, risk, diagnosis, scheduling, feedback, insights, demo

app = FastAPI(title="Agentic AI – Predictive Maintenance Demo")

# --- ROUTES ---
app.include_router(sensors.router, prefix="/sensors")
app.include_router(risk.router, prefix="/risk")
app.include_router(diagnosis.router, prefix="/diagnosis")
app.include_router(scheduling.router, prefix="/scheduling")
app.include_router(feedback.router, prefix="/feedback")
app.include_router(insights.router, prefix="/insights")
app.include_router(demo.router, prefix="/demo")


@app.get("/")
def root():
    return {
        "message": "Agentic AI – Predictive Maintenance System Running",
        "mode": "Demo Ready"
    }


@app.get("/health")
def health():
    return {"status": "OK"}
