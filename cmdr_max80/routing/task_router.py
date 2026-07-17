import json
from pathlib import Path

class TaskRouter:
    def __init__(self):
        self.base = Path(__file__).parent
        self.root = self.base.parent
        self.protocol_map = self.load_json(self.root / "protocols" / "protocol_map.json")
        self.authority_map = self.load_json(self.root / "authority" / "authority.json")
        self.eco_core = self.load_json(self.root / "ecosystem_core" / "ecosystem_core.json")
        self.stability = self.load_json(self.root / "ecosystem_core" / "stability.json", required=False)
        self.comm_flow = self.load_json(self.root / "ecosystem_core" / "communication_flow.json", required=False)

    def load_json(self, path, required=True):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            if required:
                return {"protocols": {}, "routing_rules": {"fallback_protocol": "OBSERVE"}}
            return {}
        except Exception as e:
            print(f"Failed to load {path}: {e}")
            return {}

    def check_stability(self):
        if not self.stability:
            return True
        return self.stability.get("core_integrity", "stable") == "stable"

    def check_authority(self, agent_rank, protocol_name):
        if protocol_name not in self.protocol_map.get("protocols", {}):
            return False, "Unknown protocol"
        required = self.protocol_map["protocols"][protocol_name].get("requires_authority_level", 10)
        if agent_rank < required:
            return False, f"Need {required}, have {agent_rank}"
        return True, "Authority validated"

    def route_protocol(self, protocol_name):
        protocols = self.protocol_map.get("protocols", {})
        if protocol_name not in protocols:
            fallback = self.protocol_map.get("routing_rules", {}).get("fallback_protocol", "OBSERVE")
            return fallback, f"Fallback to {fallback}"
        route = protocols[protocol_name].get("route_to", "observer")
        return route, f"Routing {protocol_name} -> {route}"

    def select_channel(self, protocol_name):
        if not self.comm_flow:
            return "observer_channel", "Default observer"
        flow = self.comm_flow.get("message_flow", {}).get(protocol_name)
        if not flow:
            return "observer_channel", "Default observer"
        return flow.get("to", "observer_channel"), f"Channel {flow.get('to')}"

    def route(self, intent):
        agent_rank = intent.get("agent_rank", 1)
        protocol = intent.get("protocol", "INIT")
        if not self.check_stability():
            return {"status": "held", "reason": "Core unstable", "protocol": protocol}
        ok, auth_msg = self.check_authority(agent_rank, protocol)
        if not ok:
            return {"status": "rejected", "reason": auth_msg, "protocol": protocol}
        route, route_msg = self.route_protocol(protocol)
        channel, channel_msg = self.select_channel(protocol)
        return {
            "status": "routed",
            "protocol": protocol,
            "route_to": route,
            "channel": channel,
            "messages": {
                "authority": auth_msg,
                "routing": route_msg,
                "channel": channel_msg
            },
            "payload": intent.get("payload", {})
        }

if __name__ == "__main__":
    router = TaskRouter()
    test_intent = {"agent_rank": 9, "protocol": "EXEC", "payload": {"task": "deploy_unit"}}
    print(json.dumps(router.route(test_intent), indent=2))
