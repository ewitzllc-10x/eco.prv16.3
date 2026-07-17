import os
import importlib.util

class AgentLoader:
    def __init__(self):
        self.base = os.path.expanduser("~")
        self.core_dir = os.path.join(self.base, "ecosystem_core")
        self.version = "1.6.3 pro16v3erbs"
        self.expected_agents = 4
        self.boot_order = ["adm_ewitz", "cmdr_max80", "cpt_eco", "1lt_act"]
        self.rank_map = {
            "adm_ewitz": 10,
            "cmdr_max80": 9.5,
            "cpt_eco": 9,
            "1lt_act": 8
        }
        self.file_map = {
            "adm_ewitz": "adm_ewitz/adm_ewitz.py",
            "cmdr_max80": "cmdr_max80/cmdr_max80.py",
            "cpt_eco": "cpt_eco/cpt_eco.py",
            "1lt_act": "1lt_act/1lt_act.py"
        }
        self.class_map = {
            "adm_ewitz": "AdmEwitz",
            "cmdr_max80": "CmdrMax80",
            "cpt_eco": "CptEco",
            "1lt_act": "LtAct"
        }
        self.loaded_agents = {}

    def discover_agents(self):
        found = []
        for agent_id in self.boot_order:
            path = os.path.join(self.base, self.file_map[agent_id])
            if os.path.exists(path):
                found.append(agent_id)
        print(f"Discovering...\n{found}")
        return found

    def load_all_agents(self):
        print("\nLoading...")
        print(f"[LOADER v1.6.3] Chain: {' -> '.join(self.boot_order)}")
        results = []
        for agent_id in self.boot_order:
            path = os.path.join(self.base, self.file_map[agent_id])
            class_name = self.class_map[agent_id]
            rank = self.rank_map[agent_id]
            
            if not os.path.exists(path):
                print(f"⚠  {agent_id} not found - {path}")
                continue
            
            try:
                spec = importlib.util.spec_from_file_location(agent_id, path)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                cls = getattr(mod, class_name)
                instance = cls()
                self.loaded_agents[agent_id] = instance
                msg = f"✔ Loaded {agent_id} (rank {rank}) - class {class_name}"
                print(msg)
                results.append(msg)
            except Exception as e:
                print(f"❌ Failed {agent_id}: {e}")
                
        status = {
            "version": self.version,
            "agents_loaded": list(self.loaded_agents.keys()),
            "expected": self.expected_agents,
            "loaded": len(self.loaded_agents),
            "chain": "adm_ewitz(10) -> cmdr_max80(9.5) -> cpt_eco(9) -> 1lt_act(8)",
            "operational": len(self.loaded_agents) == self.expected_agents
        }
        print(f"\nStatus:\n{status}")
        return results

if __name__ == "__main__":
    loader = AgentLoader()
    loader.discover_agents()
    loader.load_all_agents()
