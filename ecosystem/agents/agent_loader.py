from agents.base_agent import BaseAgent

class AgentLoader:
    def __init__(self, global_data):
        self.global_data = global_data

    def load(self, card):
        # Build a simple agent from the card
        agent = BaseAgent(
            name=card.name,
            division=card.division,
            tier=card.tier,
            auth=card.auth,
            global_data=self.global_data
        )
        return agent
