from app.core.db import get_db


class InsightsAgent:
    """
    Responsible for:
    - Computing business metrics
    - Manufacturing insights
    """

    def get_summary(self):
        conn = get_db()
        cursor = conn.cursor()

        # Count total assets (static demo assumption)
        total_assets = 4

        # Jobs
        cursor.execute("SELECT COUNT(*) FROM jobs")
        jobs_scheduled = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM jobs WHERE status='COMPLETED'")
        jobs_completed = cursor.fetchone()[0]

        # High risk assets simulated (computed dynamically elsewhere)
        high_risk_assets = 1 if jobs_scheduled > 0 else 0

        # Fake failure rate logic
        failure_rate = round((jobs_completed / jobs_scheduled), 2) if jobs_scheduled else 0.0

        conn.close()

        return {
            "total_assets": total_assets,
            "high_risk_assets": high_risk_assets,
            "jobs_scheduled": jobs_scheduled,
            "jobs_completed": jobs_completed,
            "failure_rate": failure_rate
        }
