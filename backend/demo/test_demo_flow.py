from app.agents.orchestrator import OrchestratorAgent
from demo.seed_demo_data import reset_database


def test_full_demo_flow():
    """
    Full deterministic pipeline test:
    Sensor → Risk → Diagnosis → Scheduling → Feedback → Insight
    """
    reset_database()
    orchestrator = OrchestratorAgent()

    # Run pipeline
    results = orchestrator.run_system_cycle()

    # Pick sample asset
    asset = results[0]

    assert "risk" in asset
    assert "sensor" in asset

    # Schedule if severe
    if asset["risk"]["risk_level"] in ["HIGH", "CRITICAL"]:
        job = orchestrator.schedule_maintenance(
            asset["sensor"]["asset_id"],
            asset["risk"]["risk_level"]
        )

        assert job["status"] == "SCHEDULED"

        # Log feedback
        feedback = orchestrator.log_feedback(job["job_id"], {
            "outcome": "Fixed",
            "resolved": True,
            "comments": "Replaced faulty component"
        })

        assert feedback["status"] == "Feedback logged"

    # Insights should always work
    insights = orchestrator.get_insights()
    assert "jobs_scheduled" in insights
    assert "failure_rate" in insights
