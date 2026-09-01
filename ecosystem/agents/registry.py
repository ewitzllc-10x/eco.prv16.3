from agents.cpt_ops import CptOps
from agents.cmdr_max80 import CmdrMax80

def load_agents(global_data):
    return {
        "cpt_ops": CptOps(global_data),
        "cmdr_max80": CmdrMax80(global_data)
    }
