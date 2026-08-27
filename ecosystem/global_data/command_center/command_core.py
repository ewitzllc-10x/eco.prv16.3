from missions.mission_validator import MissionValidator
from missions.mission_router import MissionRouter
from command_center.command_router import CommandRouter
from command_center.command_auth import CommandAuth

class CommandCore:
    def __init__(self, global_data):
        self.global_data = global_data

        self.validator = MissionValidator(global_data)
        self.router = MissionRouter(global_data)
        self.auth = CommandAuth(global_data)
        self.command_router = CommandRouter(global_data, self.router)

    def process(self, packet_dict):
        ok, msg = self.validator.validate(packet_dict)

        if not ok:
            self.log_error(f"Validation failed: {msg}")
            return False, msg

        division = packet_dict["division"]

        if not self.auth.can_dispatch(division):
            self.log_error(f"Unauthorized dispatch attempt by {division}")
            return False, "Unauthorized dispatch"

        return self.command_router.route(packet_dict)

    def log_error(self, text):
        with open(self.global_data["logs"]["errors"], "a") as f:
            f.write(f"[ERROR] {text}\n")
