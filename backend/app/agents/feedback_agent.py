from app.core.db import get_db


class FeedbackAgent:
    """
    Responsible for:
    - Logging job feedback
    - Updating job state
    """

    def log_feedback(self, job_id: str, data: dict):
        conn = get_db()
        cursor = conn.cursor()

        # Insert feedback record
        cursor.execute("""
            INSERT INTO feedback (job_id, outcome, resolved, comments)
            VALUES (?, ?, ?, ?)
        """, (
            job_id,
            data.get("outcome"),
            int(data.get("resolved", False)),
            data.get("comments", "")
        ))

        # Update job status
        if data.get("resolved"):
            cursor.execute("""
                UPDATE jobs SET status='COMPLETED'
                WHERE job_id=?
            """, (job_id,))
        else:
            cursor.execute("""
                UPDATE jobs SET status='FAILED'
                WHERE job_id=?
            """, (job_id,))

        conn.commit()
        conn.close()

        return {"status": "Feedback logged"}
