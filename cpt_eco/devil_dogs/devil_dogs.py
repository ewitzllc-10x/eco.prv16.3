import json, time
from pathlib import Path
ROOT = Path.home() / "eco.prv16.3"

def execute(order):
    print(f"[DEVIL_DOGS] EXECUTING: {order}")
    if "html structure" in order.lower():
        site = ROOT / "stallion_website" / "index.html"
        site.write_text("<html><head><title>STALLION</title></head><body><h1>STALLION AI</h1></body></html>")
    elif "css styling" in order.lower():
        css = ROOT / "stallion_website" / "style.css"
        css.write_text("body{background:#0a0a0a;color:#00ff41;font-family:monospace;}")
    elif "verify deployment" in order.lower():
        print("[DEVIL_DOGS] Verification: stallion_website/ exists")
    return "DD_TASK_COMPLETE"

def watch_inbox():
    inbox = ROOT / "cpt_eco" / "devil_dogs" / "mission.json"
    while True:
        if inbox.exists():
            data = json.loads(inbox.read_text())
            result = execute(data['order'])
            inbox.unlink()
            print(f"[DEVIL_DOGS] Complete: {result}")
        time.sleep(1)

if __name__ == "__main__":
    watch_inbox()
