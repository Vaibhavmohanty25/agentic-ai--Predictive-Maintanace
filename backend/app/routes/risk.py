from fastapi import APIRouter
from app.agents.orchestrator import OrchestratorAgent

router = APIRouter()
orchestrator = OrchestratorAgent()


@router.get("/{asset_id}")
def get_risk(asset_id: str):
    """
    Returns only the risk score for a selected asset.
    """
    result = orchestrator.analyze_asset(asset_id)
    return result.get("risk", {"error": "Asset not found"})
