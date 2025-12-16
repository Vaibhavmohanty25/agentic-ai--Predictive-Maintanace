from fastapi import APIRouter
from app.agents.orchestrator import OrchestratorAgent
from pydantic import BaseModel

router = APIRouter()
orchestrator = OrchestratorAgent()


class ScheduleRequest(BaseModel):
    asset_id: str
    severity: str


@router.post("/job")
def schedule_job(request: ScheduleRequest):
    """
    Creates a maintenance job using Scheduling Agent.
    """
    return orchestrator.schedule_maintenance(request.asset_id, request.severity)


@router.get("/jobs")
def list_jobs():
    """
    Returns all scheduled jobs.
    """
    from app.core.db import get_db

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs")
    data = cursor.fetchall()
    conn.close()

    return [dict(row) for row in data]
