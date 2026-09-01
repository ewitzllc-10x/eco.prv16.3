class MedicDivision:
    def __init__(self, global_data):
        self.global_data = global_data

    def execute(self, packet):
        mission_id = packet["mission_id"]
        payload = packet["payload"]
        mission_type = payload.get("type", "")

        return f"[medic_division] Medic responding to mission {mission_id} (type={mission_type})"
