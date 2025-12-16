import random
from datetime import datetime, timezone
from app.core import config
from app.core.models import SensorReading

ASSETS = ["MACHINE_1", "MACHINE_2", "MACHINE_3", "MACHINE_4"]


def generate_sensor(asset_id):
    # Read current demo mode dynamically
    demo_mode = config.DEMO_MODE
    
    # Use current time as seed for varied but reproducible results
    random.seed(int(datetime.now().timestamp()) % 1000 + hash(asset_id) % 100)
    
    base_temp = random.randint(50, 65)
    base_vibration = random.uniform(0.5, 1.2)
    base_pressure = random.randint(90, 110)
    base_rpm = random.randint(1300, 1500)

    # Force anomalies in failure mode for MACHINE_2
    if demo_mode == "failure" and asset_id == "MACHINE_2":
        base_temp = random.randint(88, 98)
        base_vibration = random.uniform(3.2, 4.5)
        base_pressure = random.randint(75, 82)
        base_rpm = random.randint(1560, 1620)

    return SensorReading(
        asset_id=asset_id,
        timestamp=datetime.now(timezone.utc),
        temperature=base_temp,
        vibration=round(base_vibration, 2),
        pressure=base_pressure,
        rpm=base_rpm,
        mode=demo_mode
    )


def get_live_sensors():
    return [generate_sensor(a) for a in ASSETS]
