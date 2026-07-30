import json, time
from pathlib import Path
ROOT = Path.home() / "eco.prv16.3"

def execute(order):
    print(f"[1LT_ACTION] Tactical plan for: {order[:50]}...")
    
    if "stallion_website" in order.lower():
        subtasks = [
            "2LT_DEVIL_DOG create html structure",
            "2LT_DEVIL_DOG add css styling",
            "2LT_DEVIL_DOG verify deployment"
        ]
        for task in subtasks:
            dog_mission = ROOT / "cpt_eco" / "2lt_devil_dog" / "mission.json"
            dog_mission.parent.mkdir(parents=True, exist_ok=True)
            dog_mission.write_text(json.dumps({"from":"1LT_ACTION","order":task}))
            print(f"[1LT_ACTION->2LT_DEVIL_DOG] Dispatched: {task}")
            time.sleep(1)
        return "1LT_ACTION_TACTICAL_COMPLETE"
    return "1LT_ACTION_ACK"
