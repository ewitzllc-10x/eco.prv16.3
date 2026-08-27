class MissionRouter:
    def __init__(self, global_data):
        self.global_data = global_data

    def process(self, packet):
        mission_id = packet["mission_id"]
        division = packet["division"]
        return True, f"Division {division} processed mission {mission_id}"
