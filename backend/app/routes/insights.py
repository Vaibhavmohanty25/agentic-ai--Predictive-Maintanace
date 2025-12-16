from fastapi import APIRouter
from app.agents.orchestrator import OrchestratorAgent

router = APIRouter()
orchestrator = OrchestratorAgent()


@router.get("/summary")
def get_summary():
    """
    Returns business metrics for dashboard.
    """
    return orchestrator.get_insights()
