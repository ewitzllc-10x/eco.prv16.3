import json, time
from pathlib import Path
ROOT = Path.home() / "eco.prv16.3"

def execute(order):
    print(f"[2LT_DEVIL_DOG] Assigning to Devil Dogs: {order[:50]}...")
    dd_mission = ROOT / "cpt_eco" / "devil_dogs" / "mission.json"
    dd_mission.parent.mkdir(parents=True, exist_ok=True)
    dd_mission.write_text(json.dumps({"from":"2LT_DEVIL_DOG","order":order}))
    return "2LT_DEVIL_DOG_ASSIGNED_TO_DD"

def watch_inbox():
    inbox = ROOT / "cpt_eco" / "2lt_devil_dog" / "mission.json"
    print(f"[2LT_DEVIL_DOG] WATCHING: {inbox}")
    while True:
        if inbox.exists():
            data = json.loads(inbox.read_text())
            result = execute(data['order'])
            inbox.unlink()
            print(f"[2LT_DEVIL_DOG] Complete: {result}")
        time.sleep(2)

if __name__ == "__main__":
    watch_inbox()
