class BaseDivision:
    def __init__(self, name, global_data):
        self.name = name
        self.global_data = global_data

        # Load division intelligence profile
        profiles = global_data["divisions"].get("intelligence_profiles", {})
        self.profile = profiles.get(name, {})

        # Personality (aggressive, cautious, analytical, calm)
        self.personality = self.profile.get("personality", "neutral")

        # Specialization (tactics, analysis, scanning, triage)
        self.specialization = self.profile.get("specialization", "general")

        # Skill levels
        self.skills = self.profile.get("skills", {
            "tactics": 1,
            "analysis": 1,
            "scanning": 1,
            "triage": 1
        })

    def log(self, text):
        print(f"[{self.name.upper()}] {text}")

    def choose_behavior(self, packet):
        """Division chooses behavior based on specialization + mission."""
        mission_type = packet["payload"].get("type", "standard")
        threat = packet["payload"].get("threat_level", 0)

        if self.specialization == "tactics":
            if threat >= 7:
                return "execute_high_threat_protocol"
            return "execute_standard_protocol"

        if self.specialization == "analysis":
            return "perform_intel_analysis"

        if self.specialization == "scanning":
            return "perform_recon_scan"

        if self.specialization == "triage":
            return "perform_medical_triage"

        return "general_support"
