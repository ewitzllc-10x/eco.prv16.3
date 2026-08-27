from divisions.ops_division import OpsDivision
from divisions.intel_division import IntelDivision
from divisions.recon_division import ReconDivision
from divisions.medic import MedicDivision
from divisions.grunts import GruntsDivision

def load_divisions(global_data):
    return {
        "ops_division": OpsDivision(global_data),
        "intel_division": IntelDivision(global_data),
        "recon_division": ReconDivision(global_data),
        "medic": MedicDivision(global_data),
        "grunts": GruntsDivision(global_data)
    }
