import uuid
from datetime import datetime, timedelta
from app.core.db import get_db


class SchedulingAgent:
    """
    Responsible for:
    - Scheduling maintenance jobs
    - Assigning time slots
    - Persisting jobs
    """

    def create_job(self, asset_id: str, severity: str):
        job_id = str(uuid.uuid4())

        now = datetime.utcnow()

        # --- Severity based scheduling ---
        if severity == "CRITICAL":
            scheduled = now + timedelta(hours=1)
        elif severity == "HIGH":
            scheduled = now + timedelta(hours=8)
        elif severity == "MEDIUM":
            scheduled = now + timedelta(days=2)
        else:
            scheduled = now + timedelta(days=5)

        technician = "AUTO_ASSIGNED_TECH"

        # --- Store in database ---
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO jobs (job_id, asset_id, scheduled_time, technician, status)
            VALUES (?, ?, ?, ?, ?)
        """, (job_id, asset_id, scheduled.isoformat(), technician, "SCHEDULED"))
        conn.commit()
        conn.close()

        return {
            "job_id": job_id,
            "asset_id": asset_id,
            "scheduled_time": scheduled.isoformat(),
            "technician": technician,
            "status": "SCHEDULED"
        }
