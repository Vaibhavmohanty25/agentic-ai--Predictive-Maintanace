class DiagnosisAgent:
    """
    Responsible for:
    - Interpreting risk signals
    - Applying rule-based diagnosis
    - Producing explainable results
    """

    def diagnose(self, reading, risk):
        rules = []
        issue = "No major issue detected"
        severity = risk["risk_level"]
        recommendations = []

        # --- Rule Engine ---
        if reading.temperature > 90 and reading.vibration > 3:
            issue = "Bearing failure likely"
            rules.append("TEMP>90 and VIBRATION>3")
            recommendations.append("Stop machine and inspect bearings")
            recommendations.append("Schedule immediate maintenance")

        elif reading.temperature > 85:
            issue = "Overheating detected"
            rules.append("TEMP>85")
            recommendations.append("Inspect cooling system")
            recommendations.append("Reduce load temporarily")

        elif reading.vibration > 3:
            issue = "Mechanical imbalance or misalignment"
            rules.append("VIBRATION>3")
            recommendations.append("Check shaft alignment")
            recommendations.append("Inspect rotating components")

        elif reading.pressure < 85:
            issue = "Low pressure anomaly"
            rules.append("PRESSURE<85")
            recommendations.append("Check hydraulic systems")

        elif reading.rpm > 1550:
            issue = "RPM overspeed"
            rules.append("RPM>1550")
            recommendations.append("Check control systems")

        # --- Default recommendation for high risk ---
        if severity in ["HIGH", "CRITICAL"] and not recommendations:
            recommendations.append("Schedule inspection within 24 hours")

        return {
            "asset_id": reading.asset_id,
            "probable_issue": issue,
            "severity": severity,
            "rules_triggered": rules,
            "recommendations": recommendations
        }
