def build_agent_card(name, division, tier="LTD-1"):
    return {
        "identity": {
            "name": name,
            "division": division,
            "tier": tier
        },
        "auth": {
            "level": "standard"
        }
    }
