from divisions.base_division import BaseDivision

class GruntsDivision(BaseDivision):
    def __init__(self, global_data):
        super().__init__("grunts", global_data)

    def process(self, packet):
        self.log(f"Grunts executing mission {packet['mission_id']}")
        return True, "GruntsDivision completed mission"
