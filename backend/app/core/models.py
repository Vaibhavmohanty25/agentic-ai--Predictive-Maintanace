from pydantic import BaseModel
from typing import List
from datetime import datetime


class SensorReading(BaseModel):
    asset_id: str
    timestamp: datetime
    temperature: float
    vibration: float
    pressure: float
    rpm: int
    mode: str


class RiskScore(BaseModel):
    asset_id: str
    risk_score: float
    risk_level: str
    factors: List[str]


class Diagnosis(BaseModel):
    asset_id: str
    probable_issue: str
    severity: str
    rules_triggered: List[str]
    recommendations: List[str]


class MaintenanceJob(BaseModel):
    job_id: str
    asset_id: str
    scheduled_time: datetime
    technician: str
    status: str


class Feedback(BaseModel):
    job_id: str
    outcome: str
    resolved: bool
    comments: str = ""


class InsightSummary(BaseModel):
    total_assets: int
    high_risk_assets: int
    jobs_scheduled: int
    jobs_completed: int
    failure_rate: float
