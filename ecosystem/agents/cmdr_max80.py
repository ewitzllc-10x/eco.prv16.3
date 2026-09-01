class CmdrMax80:
    def __init__(self, global_data):
        self.global_data = global_data

    def act(self, packet):
        mission_id = packet["mission_id"]
        payload = packet["payload"]
        mission_type = payload.get("type", "")
        threat = payload.get("threat_level", 0)

        return f"[cmdr_max80] Commander Max80 coordinating mission {mission_id} (type={mission_type}, threat={threat})"
