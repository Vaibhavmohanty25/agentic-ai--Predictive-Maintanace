from fastapi import APIRouter
import os
from app.core import config

router = APIRouter()


@router.post("/mode/{mode}")
def set_demo_mode(mode: str):
    """
    Switch demo mode between:
    - normal
    - failure
    """
    if mode not in ["normal", "failure"]:
        return {"error": "Mode must be 'normal' or 'failure'"}

    os.environ["DEMO_MODE"] = mode
    config.DEMO_MODE = mode

    return {"message": f"Demo mode set to {mode}"}


@router.post("/reset")
def reset_demo():
    """
    Resets demo state.
    """
    from demo.seed_demo_data import reset_database
    reset_database()

    return {"message": "Demo reset completed"}
