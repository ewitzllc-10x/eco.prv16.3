class BaseAgent:
    def __init__(self, card, global_data):
        self.card = card
        self.global_data = global_data
        self.logs = global_data["logs"]

        # Load agent intelligence profile
        self.profile = global_data["agents"].get(self.card["identity"]["name"], {})

        # Personality traits
        self.personality = self.profile.get("personality", "neutral")

        # Specialization (combat, recon, intel, medic)
        self.specialization = self.profile.get("specialization", "general")

        # Skill levels
        self.skills = self.profile.get("skills", {
            "combat": 1,
            "recon": 1,
            "intel": 1,
            "medical": 1
        })

    def log(self, text):
        name = self.card["identity"]["name"].upper()
        with open(self.logs["agents"], "a") as f:
            f.write(f"[{name}] {text}\n")

    def choose_action(self, mission):
        """Agent chooses an action based on specialization + mission type."""
        mission_type = mission["payload"].get("type", "standard")
        threat = mission["payload"].get("threat_level", 0)

        # Specialization-based decision
        if self.specialization == "combat":
            if threat >= 7:
                return "engage_high_threat"
            return "secure_area"

        if self.specialization == "recon":
            return "perform_scouting"

        if self.specialization == "intel":
            return "analyze_data"

        if self.specialization == "medic":
            return "provide_medical_support"

        # Default fallback
        return "support_operation"

    def execute(self, mission):
        action = self.choose_action(mission)

        self.log(f"Executing action: {action} | personality={self.personality}")

        return True, f"Agent {self.card['identity']['name']} performed action: {action}"
