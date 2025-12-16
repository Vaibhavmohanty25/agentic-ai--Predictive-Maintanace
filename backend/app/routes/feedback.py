from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.orchestrator import OrchestratorAgent

router = APIRouter()
orchestrator = OrchestratorAgent()


class FeedbackRequest(BaseModel):
    job_id: str
    outcome: str
    resolved: bool
    comments: str = ""


@router.post("/")
def submit_feedback(request: FeedbackRequest):
    """
    Submits technician feedback.
    """
    data = request.dict()
    return orchestrator.log_feedback(request.job_id, data)
