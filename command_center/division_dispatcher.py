
import os
import json
import time
import re

BASE_PATH = os.path.expanduser("~/eco.prv16.3/ecosystem")

def load_packet(packet):
    if not isinstance(packet, dict):
        raise ValueError("packet must be dict")
    packet.setdefault("history", [])
    packet.setdefault("status", "new")
    return {"packet": packet, "status": "loaded"}

def identify_division(packet):
    # pull from top-level or inside mission
    division = packet.get("division") or packet.get("mission", {}).get("division") or "unassigned"
    division = str(division).strip()
    # block traversal but keep your path logic
    division = division.replace("/", "_").replace("\\", "_").replace("..", "_")
    if not division:
        division = "unassigned"
    return {"division": division, "status": "division_identified"}

def handoff_to_division(packet, division):
    base_path = BASE_PATH  # YOUR PATH - NOT CHANGED
    division_path = os.path.join(base_path, division)
    os.makedirs(division_path, exist_ok=True)

    # safe filename with type + timestamp + id to avoid overwrite
    m_type = packet.get("mission", {}).get("type", "unknown")
    m_type = re.sub(r"[^a-zA-Z0-9_-]", "_", str(m_type))[:40]
    mission_id = packet.get("id") or packet.get("mission", {}).get("id") or int(time.time())
    filename = f"mission_{m_type}_{mission_id}.json"
    filepath = os.path.join(division_path, filename)

    # write + verify
    with open(filepath, "w") as f:
        json.dump(packet, f, indent=4)

    # confirm it landed
    assert os.path.exists(filepath)

    return {"handoff": True, "path": filepath, "division": division}

def update_status(packet, status):
    packet["status"] = status
    packet.setdefault("history", [])
    packet["history"].append(f"{status}@{int(time.time())}")
    return {"packet": packet, "status": "updated"}

def dispatch(packet):
    """One call to rule them all"""
    p = load_packet(packet)["packet"]
    d = identify_division(p)["division"]
    h = handoff_to_division(p, d)
    u = update_status(p, f"handed_to_{d}")
    # also write the updated status back to disk
    with open(h["path"], "w") as f:
        json.dump(u["packet"], f, indent=4)
    return h

def dispatch(packet):
    """
    Full dispatcher pipeline.
    """
    # Step 1: Load
    loaded = load_packet(packet)

    # Step 2: Identify division
    division_info = identify_division(packet)
    division = division_info["division"]

    # Step 3: Update status
    update_status(packet, "division_identified")

    # Step 4: Handoff
    handoff = handoff_to_division(packet, division)

    # Step 5: Final status update
    update_status(packet, "dispatched")

    return {
        "status": "dispatched",
        "division": division,
        "path": handoff["path"]
    }
