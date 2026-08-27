from global_data.global_loader import load_global_data
from divisions.division_registry import load_divisions
from agents.registry import load_agents
from command_center.validator import MissionValidator


class CommandCore:
    def __init__(self, global_data):
        self.global_data = global_data

        # Load divisions and agents
        self.divisions = load_divisions(self.global_data)
        self.agents = load_agents(self.global_data)

        # Validator
        self.validator = MissionValidator(self.global_data)

    def select_division(self, packet):
        """Smart division routing based on mission type and payload."""
        mission_type = packet["payload"].get("type", "standard")
        threat = packet["payload"].get("threat_level", 0)

        # High‑threat missions → ops
        if threat >= 8:
            return "ops_division"

        # Intel missions → intel
        if mission_type in ["intel", "surveillance"]:
            return "intel_division"

        # Recon missions → recon
        if mission_type in ["recon", "scout"]:
            return "recon_division"

        # Default fallback
        return packet["division"]

    def select_agent(self, packet, division_result):
        """Smart agent selection based on division output and mission payload."""
        payload = packet["payload"]
        threat = payload.get("threat_level", 0)

        # If division recommended an agent
        if "recommended agent" in division_result.lower():
            # Extract agent name from the division result
            parts = division_result.split("recommended agent:")
            if len(parts) > 1:
                return parts[1].strip()

        # High threat → grunt_X
        if threat >= 8:
            return "grunt_X"

        # Medium threat → cmdr_max80
        if threat >= 4:
            return "cmdr_max80"

        # Low threat → first agent
        return list(self.agents.keys())[0]

    def process(self, packet):
        # 1. Validate mission
        ok, msg = self.validator.validate(packet)
        if not ok:
            return False, msg

        # 2. Smart division routing
        division_name = self.select_division(packet)
        division = self.divisions.get(division_name)

        if division is None:
            return False, f"Unknown division: {division_name}"

        # 3. Division executes mission
        ok, division_result = division.process(packet)
        if not ok:
            return False, division_result

        # 4. Smart agent selection
        agent_name = self.select_agent(packet, division_result)
        agent = self.agents.get(agent_name)

        if agent is None:
            return False, f"Unknown agent: {agent_name}"

        # 5. Agent executes mission
        ok, agent_result = agent.execute(packet)
        if not ok:
            return False, agent_result

        # 6. Final combined result
        return True, f"{division_result} | {agent_result}"
