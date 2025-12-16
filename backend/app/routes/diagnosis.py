from fastapi import APIRouter
from app.agents.orchestrator import OrchestratorAgent

router = APIRouter()
orchestrator = OrchestratorAgent()


@router.get("/{asset_id}")
def get_diagnosis(asset_id: str):
    """
    Returns diagnosis + risk + sensor data for an asset.
    """
    result = orchestrator.analyze_asset(asset_id)
    return result
