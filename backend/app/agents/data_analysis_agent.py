class DataAnalysisAgent:
    """
    Responsible for:
    - Risk scoring
    - Failure probability
    - Factor extraction
    """

    def evaluate_risk(self, reading):
        factors = []
        score = 0.1

        # --- Temperature logic ---
        if reading.temperature > 85:
            score += 0.4
            factors.append("High temperature")
        elif reading.temperature > 70:
            score += 0.2
            factors.append("Elevated temperature")

        # --- Vibration logic ---
        if reading.vibration > 3.0:
            score += 0.4
            factors.append("Critical vibration level")
        elif reading.vibration > 2.0:
            score += 0.2
            factors.append("Abnormal vibration")

        # --- Pressure logic ---
        if reading.pressure < 85 or reading.pressure > 115:
            score += 0.2
            factors.append("Pressure anomaly")

        # --- RPM logic ---
        if reading.rpm > 1550 or reading.rpm < 1200:
            score += 0.2
            factors.append("RPM out of range")

        # --- Normalize score ---
        score = min(score, 1.0)

        # --- Risk levels ---
        if score >= 0.85:
            level = "CRITICAL"
        elif score >= 0.65:
            level = "HIGH"
        elif score >= 0.4:
            level = "MEDIUM"
        else:
            level = "LOW"

        return {
            "asset_id": reading.asset_id,
            "risk_score": round(score, 2),
            "risk_level": level,
            "factors": factors
        }
