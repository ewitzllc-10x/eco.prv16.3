from command_center.command_core import CommandCore
from global_data.global_loader import load_global_data

def main():
    global_data = load_global_data()
    core = CommandCore(global_data)

    # Example mission packet
    packet = {
        "mission_id": "M-001",
        "division": "ops_division",
        "payload": {"task": "test_run"},
        "checksum": "ok",
        "timestamp": "now"
    }

    ok, result = core.process(packet)
    print(result)

if __name__ == "__main__":
    main()
