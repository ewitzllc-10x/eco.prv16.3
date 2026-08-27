from agents.agent_card import build_agent_card
from agents.base_agent import BaseAgent

def load_agents(global_data):
    agents = {}

    # Load agent definitions from global.json
    agent_profiles = global_data["agents"]

    for agent_name, profile in agent_profiles.items():
        # Build agent card dynamically
        card = build_agent_card(
            name=agent_name,
            division=profile.get("role", "general"),
            tier=profile.get("priority", "LTD-1")
        )

        # Create agent instance
        agent = BaseAgent(card, global_data)
        agents[agent_name] = agent

    return agents
