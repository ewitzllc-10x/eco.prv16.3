class MissionValidator:
    def __init__(self, global_data):
        self.global_data = global_data

    def validate(self, packet):
        required = ["mission_id", "division", "payload"]

        for field in required:
            if field not in packet:
                return False, f"Missing field: {field}"

        return True, "Mission validated"
