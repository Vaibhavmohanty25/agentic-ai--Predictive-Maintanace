class VoiceAgent:
    """
    Optional voice interface placeholder.
    This exists to show extensibility for:
    - Speech Recognition
    - Voice commands
    """

    def interpret_command(self, text: str):
        """
        Accepts text (simulated voice input)
        """
        text = text.lower()

        if "status" in text:
            return {"intent": "GET_STATUS"}

        if "schedule" in text:
            return {"intent": "SCHEDULE"}

        if "risk" in text:
            return {"intent": "GET_RISK"}

        return {"intent": "UNKNOWN"}
