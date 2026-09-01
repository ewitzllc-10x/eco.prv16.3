
# mission_router.py

 def parse_mission(raw):
    """
    Convert raw mission input into a structured dict.
    """
    mission = {
        "type": raw.get("type", None),
        "payload": raw.get("payload", {}),
        "priority": raw.get("priority", "normal"),
        "requester": raw.get("requester", "unknown"),
        "tags": raw.get("tags", [])
    }
    return mission

def validate_mission(mission):
    """
    Ensure mission contains required fields.
    """
    required = ["type", "payload", "priority", "requester"]

    for field in required:
        if mission.get(field) is None:
            return {
                "valid": False,
                "error": f"Missing required field: {field}"
            }

    return {"valid": True}

def classify_mission(mission):
    """
    Determine mission type and risk level.
    """
    mission_type = mission.get("type", "unknown")

    # Simple risk logic for now
    priority = mission.get("priority", "normal")
    risk = "low"

    if priority == "high":
        risk = "medium"
    if priority == "critical":
        risk = "high"

    return {
        "type": mission_type,
        "risk": risk
    }
    pass

def map_division(mission_type, risk):
    """
    Map mission type to a division.
    Simple placeholder logic until full division rules are added.
    """

    division_map = {
        "ops": "operations",
        "intel": "intelligence",
        "recon": "recon_division",
        "squad": "squad_unit",
        "dr": "medic",
        "grunt": "platoon"
    }

    # Default fallback
    division = division_map.get(mission_type, "unassigned")

    return {
        "division": division,
        "risk": risk
    }
    pass

def build_packet(mission, division):
    """
    Build the mission packet that will be delivered into the ecosystem.
    """
    packet = {
        "mission": mission,
        "division": division.get("division"),
        "risk": division.get("risk"),
        "status": "routed",
        "timestamp": "TBD",  # placeholder until time module added
        "history": ["packet_created"]
    }
    return packet
    pass

def deliver_packet(packet):
    """
    Deliver the mission packet into the ecosystem inbox.
    """
    import os
    import json

    inbox_path = os.path.expanduser("~/eco.prv16.3/ecosystem/missions/inbox")

    # Ensure inbox exists
    os.makedirs(inbox_path, exist_ok=True)

    # Create filename
    filename = f"mission_{packet['mission'].get('type', 'unknown')}.json"
    filepath = os.path.join(inbox_path, filename)

    # Write packet
    with open(filepath, "w") as f:
        json.dump(packet, f, indent=4)

    return {
        "delivered": True,
        "path": filepath
    }
    pass

def enforce_security(packet):
    """
    Apply basic security checks before delivery.
    """
    # Simple placeholder logic
    allowed_divisions = [
        "operations",
        "intelligence",
        "recon_division",
        "squad_unit",
        "medic",
        "platoon",
        "unassigned"
    ]

    division = packet.get("division")

    if division not in allowed_divisions:
        return {
            "secure": False,
            "error": f"Unauthorized division: {division}"
        }

    return {"secure": True}
    pass

def route_mission(raw):
    """
    Full mission routing pipeline.
    """
    # Step 1: Parse
    mission = parse_mission(raw)

    # Step 2: Validate
    validation = validate_mission(mission)
    if not validation["valid"]:
        return {"status": "rejected", "error": validation["error"]}

    # Step 3: Classify
    classification = classify_mission(mission)

    # Step 4: Map division
    division = map_division(classification["type"], classification["risk"])

    # Step 5: Build packet
    packet = build_packet(mission, division)

    # Step 6: Security check
    security = enforce_security(packet)
    if not security["secure"]:
        return {"status": "blocked", "error": security["error"]}

    # Step 7: Deliver
    delivery = deliver_packet(packet)

    return {
        "status": "delivered",
        "packet_path": delivery["path"]
    }
    pass
