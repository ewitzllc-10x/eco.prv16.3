from agent_loader import AgentLoader
import json
class ReportEngine:
 def generate(self):
  l=AgentLoader()
  l.discover_agents()
  l.load_all_agents()
  print(json.dumps({"v":"1.6.3","loaded":len(l.loaded_agents),"operational":len(l.loaded_agents)==4},indent=2))
if __name__=="__main__":
 ReportEngine().generate()
