from fastapi import APIRouter
from app.core.mock_data import get_live_sensors

router = APIRouter()


@router.get("/live")
def get_live_sensor_data():
    """
    Returns live (mock) sensor data for all assets.
    """
    sensors = get_live_sensors()
    return {
        "count": len(sensors),
        "data": [s.dict() for s in sensors]
    }
