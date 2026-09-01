from divisions.division_registry import load_divisions
from agents.registry import load_agents
from command_center.validator import MissionValidator
from command_center.threat_engine import ThreatEngine


class CommandCore:
    def __init__(self, global_data):
        self.global_data = global_data
        self.validator = MissionValidator(self.global_data)
        self.threat_engine = ThreatEngine()
        self.divisions = load_divisions(global_data)
        self.agents = load_agents(global_data)

    def process(self, packet):
        ok, msg = self.validator.validate(packet)
        if not ok:
            return False, msg

        division = packet["division"]
        division_result = self.divisions[division].execute(packet)

        threat_score = packet["payload"].get("threat_level", 0)
        agent_name = self.select_agent(threat_score)
        agent = self.agents[agent_name]
        agent_result = agent.act(packet)

        return True, f"{division_result} | {agent_result}"

    def select_agent(self, threat_score):
        if threat_score >= 10:
            return "cmdr_max80"
        return "cpt_ops"
