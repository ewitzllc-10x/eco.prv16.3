# inbox_processor.py

def scan_inbox():
    """
    Scan the mission inbox directory and return all packet file paths.
    """
    import os

    inbox_path = os.path.expanduser("~/eco.prv16.3/ecosystem/missions/inbox")

    # Ensure inbox exists
    os.makedirs(inbox_path, exist_ok=True)

    files = []
    for f in os.listdir(inbox_path):
        if f.endswith(".json"):
            files.append(os.path.join(inbox_path, f))

    return files
    pass

def load_packet(path):
    """
    Load a mission packet JSON file from disk.
    """
    import json

    try:
        with open(path, "r") as f:
            packet = json.load(f)
        return packet
    except Exception as e:
        return {
            "error": f"Failed to load packet: {e}",
            "path": path
        }
    pass

def verify_packet(packet):
    """
    Verify that the packet contains the required fields.
    """
    required_fields = ["mission", "division", "status"]

    # Check for errors from load_packet()
    if "error" in packet:
        return {
            "valid": False,
            "reason": packet["error"]
        }

    # Check required fields
    for field in required_fields:
        if field not in packet:
            return {
                "valid": False,
                "reason": f"Missing required field: {field}"
            }

    return {
        "valid": True,
        "reason": "packet_verified"
    }
    pass

def forward_to_dispatcher(packet):
    """
    Forward a verified packet to the division dispatcher.
    """
    try:
        from eco.prv16.3.command_center.division_dispatcher import dispatch
    except Exception:
        # Fallback import for Termux relative paths
        import sys, os
        sys.path.append(os.path.expanduser("~/eco.prv16.3/command_center"))
        from division_dispatcher import dispatch

    result = dispatch(packet)

    return {
        "forwarded": True,
        "dispatcher_result": result
    }
    pass

def process_inbox():
    """
    Full inbox processing pipeline.
    """
    results = []

    # Step 1: Scan inbox
    inbox_files = scan_inbox()

    for path in inbox_files:
        # Step 2: Load packet
        packet = load_packet(path)

        # Step 3: Verify packet
        verification = verify_packet(packet)
        if not verification["valid"]:
            results.append({
                "file": path,
                "status": "invalid",
                "reason": verification["reason"]
            })
            continue

        # Step 4: Forward to dispatcher
        dispatch_result = forward_to_dispatcher(packet)

        results.append({
            "file": path,
            "status": "processed",
            "dispatcher": dispatch_result
        })

    return results
    pass
