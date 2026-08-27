from divisions.base_division import BaseDivision

class OpsDivision(BaseDivision):
    def __init__(self, global_data):
        super().__init__("ops_division", global_data)

    def process(self, packet):
        behavior = self.choose_behavior(packet)
        self.log(f"Behavior: {behavior}")
        return True, "Ops completed mission"
