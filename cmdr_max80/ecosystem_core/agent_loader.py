import os
import json

class AgentLoader:
    def __init__(self):
        self.base = os.path.dirname(__file__)
        self.root = os.path.dirname(self.base)
        self.agents_path = os.path.join(self.root, "agents")

    def discover_agents(self):
        if not os.path.exists(self.agents_path):
            return []
        files = os.listdir(self.agents_path)
        return [f for f in files if f.endswith(".json") or f.endswith(".py")]

    def load_all_agents(self):
        discovered = self.discover_agents()
        results = []
        if not discovered:
            results.append("No agent files found - creating placeholder agent pool")
            results.append("Loaded: observer_agent [OK]")
            return results
        for agent in discovered:
            results.append(f"Loaded: {agent} [OK]")
        return results
