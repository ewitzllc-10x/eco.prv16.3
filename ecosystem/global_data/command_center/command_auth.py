class CommandAuth:
    def __init__(self, global_data):
        self.authority_map = global_data["protocols"]["authority_map"]

    def can_dispatch(self, division):
        if division not in self.authority_map:
            return False
        return self.authority_map[division]["can_dispatch"]

    def get_auth_level(self, division):
        if division not in self.authority_map:
            return None
        return self.authority_map[division]["auth_level"]
