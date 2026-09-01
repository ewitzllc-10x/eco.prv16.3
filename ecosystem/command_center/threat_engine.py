class ThreatEngine:
    def __init__(self):
        # Adjustable weights for mission types
        self.base_weights = {
            "intel": 3,
            "recon": 4,
            "ops": 6,
            "medic": 2,
        }

    def score(self, packet):
        """
        Returns a numeric threat score based on payload.
        """
        payload = packet.get("payload", {})

        # Start from payload threat_level if present
        threat = payload.get("threat_level", 0)

        # Mission type
        mission_type = payload.get("type", "").lower()

        # Division hint
        division = packet.get("division", "").lower()

        # Add weight based on mission type
        if mission_type in ["intel", "surveillance"]:
            threat += self.base_weights["intel"]
        elif mission_type in ["recon", "scout"]:
            threat += self.base_weights["recon"]
        elif mission_type in ["ops", "breach", "assault"]:
            threat += self.base_weights["ops"]
        elif mission_type in ["medic", "evac"]:
            threat += self.base_weights["medic"]

        # Slight bump if division is ops
        if division == "ops_division":
            threat += 1

        return threat
