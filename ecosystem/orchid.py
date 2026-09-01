from global_data.global_loader import load_global_data
from divisions.division_registry import load_divisions
from agents.registry import load_agents
from command_center.validator import MissionValidator
from command_center.command_core import CommandCore

def main():
    global_data = load_global_data()

    divisions = load_divisions(global_data)
    agents = load_agents(global_data)
    validator = MissionValidator(global_data)

    core = CommandCore(global_data)
    packet = {
        "mission_id": "T-OPS-01",
        "division": "ops_division",
        "payload": {
            "type": "assault",
            "threat_level": 9
        }
    }

    ok, result = core.process(packet)
    print(ok, result)

if __name__ == "__main__":
    main()
