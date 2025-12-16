import os

DEMO_MODE = os.getenv("DEMO_MODE", "normal")   # normal | failure

DATABASE_URL = "sqlite:///./demo.db"

RISK_THRESHOLDS = {
    "LOW": 0.3,
    "MEDIUM": 0.6,
    "HIGH": 0.8
}
