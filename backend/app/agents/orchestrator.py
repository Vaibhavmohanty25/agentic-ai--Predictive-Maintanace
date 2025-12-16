from app.agents.data_analysis_agent import DataAnalysisAgent
from app.agents.diagnosis_agent import DiagnosisAgent
from app.agents.scheduling_agent import SchedulingAgent
from app.agents.feedback_agent import FeedbackAgent
from app.agents.insights_agent import InsightsAgent
from app.core.mock_data import get_live_sensors


class OrchestratorAgent:
    """
    Central brain of the system.
    Controls the full flow:
    Sensor → Risk → Diagnosis → Action → Feedback → Insight
    """

    def __init__(self):
        self.data_agent = DataAnalysisAgent()
        self.diagnosis_agent = DiagnosisAgent()
        self.scheduling_agent = SchedulingAgent()
        self.feedback_agent = FeedbackAgent()
        self.insights_agent = InsightsAgent()

    # --- CORE PIPELINE ---

    def run_system_cycle(self):
        """
        Executes one full agent cycle over live sensor data.
        """
        readings = get_live_sensors()
        results = []

        for reading in readings:
            risk = self.data_agent.evaluate_risk(reading)

            diagnosis = None
            if risk["risk_level"] in ["HIGH", "CRITICAL"]:
                diagnosis = self.diagnosis_agent.diagnose(reading, risk)

            results.append({
                "sensor": reading.dict(),
                "risk": risk,
                "diagnosis": diagnosis
            })

        return results

    def analyze_asset(self, asset_id: str):
        """
        Full evaluation for a single asset.
        """
        sensors = get_live_sensors()

        for s in sensors:
            if s.asset_id == asset_id:
                risk = self.data_agent.evaluate_risk(s)
                diagnosis = self.diagnosis_agent.diagnose(s, risk)
                return {
                    "sensor": s.dict(),
                    "risk": risk,
                    "diagnosis": diagnosis
                }

        return {"error": "Asset not found"}

    def schedule_maintenance(self, asset_id: str, severity: str):
        """
        Sends scheduling task to Scheduling Agent.
        """
        return self.scheduling_agent.create_job(asset_id, severity)

    def log_feedback(self, job_id: str, data: dict):
        """
        Routes feedback to Feedback Agent.
        """
        return self.feedback_agent.log_feedback(job_id, data)

    def get_insights(self):
        """
        Retrieves manufacturing insights.
        """
        return self.insights_agent.get_summary()
