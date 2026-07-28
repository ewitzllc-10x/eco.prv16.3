import sys
from pathlib import Path
import importlib.util
ROOT = Path.cwd()
sys.path.insert(0, str(ROOT))

def load_coder(path, class_name):
    spec = importlib.util.spec_from_file_location("mod", ROOT / path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, class_name)()

CPT = load_coder("cpt_eco/cpt_workflows/cpt_workflow_coder.py", "CptWorkflowCoder")
LT1 = load_coder("cpt_eco/lt1_action/lt1_workflows/workflow_coder.py", "Lt1WorkflowCoder")
LT2 = load_coder("cpt_eco/lt2_devil_dog/lt2_workflows/workflow_coder.py", "Lt2WorkflowCoder")
CMDR = load_coder("cmdr_max80/workflows/workflow.main.py", "CmdrWorkflow")

CHAIN = {
    "cpt eco": CPT, "cpt": CPT,
    "1lt": LT1, "lt1": LT1, "action": LT1,
    "2lt": LT2, "lt2": LT2, "devil": LT2,
    "cmdr": CMDR, "max80": CMDR, "cmdr max80": CMDR,
}

def route(order: str):
    low = order.lower()
    for key in sorted(CHAIN, key=len, reverse=True):
        if key in low:
            print(f"[ADM EWITZ] -> {key.upper()} | Order: {order}")
            return CHAIN[key].execute(order)
    print(f"[ADM EWITZ] FULL CHAIN ORDER: {order}")
    for name, unit in [("CPT ECO", CPT), ("1LT ACTION", LT1), ("2LT DEVIL DOG", LT2), ("CMDR MAX80", CMDR)]:
        print(f"\n--- {name} ---")
        unit.execute(order)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python3 adm_orders.py "CMDR MAX80 build Stallion website"')
        print('Examples:')
        print(' "CPT ECO design auth system"')
        print(' "1LT build API"')
        print(' "full chain build marketplace"')
        sys.exit(0)
    route(" ".join(sys.argv[1:]))
