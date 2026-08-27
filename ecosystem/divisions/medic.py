from divisions.base_division import BaseDivision

class MedicDivision(BaseDivision):
    def __init__(self, global_data):
        super().__init__("medic", global_data)

    def assess_injury(self, payload):
        """Classify injury severity."""
        severity = payload.get("injury_severity", 0)

        if severity >= 8:
            return "critical"
        elif severity >= 4:
            return "serious"
        elif severity >= 1:
            return "minor"
        return "none"

    def required_supplies(self, severity):
        """Determine medical supplies needed."""
        if severity == "critical":
            return ["medkit", "stabilizer", "oxygen"]
        if severity == "serious":
            return ["medkit", "bandages"]
        if severity == "minor":
            return ["bandages"]
        return []

    def recommend_action(self, severity, payload):
        """Recommend next steps based on medical situation."""
        threat = payload.get("threat_level", 0)

        if severity == "critical":
            if threat >= 6:
                return "ops_division"
            return "evacuation"

        if severity == "serious":
            return "intel_division" if threat >= 5 else "cmdr_max80"

        if severity == "minor":
            return "grunt_X"

        return "none"

    def process(self, packet):
        payload = packet["payload"]
        mission_id = packet["mission_id"]

        self.log(f"[MEDIC] Processing medical mission {mission_id}")

        # 1. Assess injury severity
        severity = self.assess_injury(payload)
        self.log(f"[MEDIC] Injury severity: {severity}")

        # 2. Determine required supplies
        supplies = self.required_supplies(severity)
        for s in supplies:
            self.log(f"[MEDIC] Required supply: {s}")

        # 3. Recommend next action
        recommendation = self.recommend_action(severity, payload)
        self.log(f"[MEDIC] Recommendation: {recommendation}")

        # 4. Final summary
        summary = (
            f"MedicDivision completed mission | severity={severity} | "
            f"supplies={supplies} | recommended={recommendation}"
        )

        return True, summary
