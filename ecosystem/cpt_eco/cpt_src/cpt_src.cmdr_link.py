import json, time, importlib.util
from pathlib import Path
ROOT = Path.home() / "eco.prv16.3"

def execute(order):
    print(f"[CPT_ECO] Received from CMDR: {order[:80]}...")
    log = ROOT / "logs" / "cpt_eco.log"
    log.parent.mkdir(exist_ok=True)
    
    # Delegate to LT1_ACTION
    lt1_path = ROOT / "cpt_eco" / "1lt_action" / "1lt_action.py"
    if lt1_path.exists():
        spec = importlib.util.spec_from_file_location("lt1", str(lt1_path))
        lt1 = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(lt1)
        result = lt1.execute(order)
        print(f"[CPT->LT1_ACTION] Result: {result}")
    else:
        result = f"CPT_ECO_ACK: {order[:50]}"
    
    with open(log, "a") as lf:
        lf.write(f"{time.ctime()} | ORDER: {order} | RESULT: {result}\n")
    return result

def watch_inbox():
    inbox = ROOT / "cpt_eco" / "mission.json"
    while True:
        if inbox.exists():
            data = json.loads(inbox.read_text())
            result = execute(data['order'])
            inbox.unlink()
            print(f"[CPT_ECO] Complete: {result}")
        time.sleep(5)

if __name__ == "__main__":
    watch_inbox()
