import os,json
from agent_loader import AgentLoader
from task_router import TaskRouter
class EcosystemSync:
 def sync(self):
  b=os.path.dirname(__file__)
  comm=json.load(open(os.path.join(b,"communication_flow.json")))
  loader=AgentLoader()
  loader.discover_agents()
  loader.load_all_agents()
  print("OPERATIONAL" if len(loader.loaded_agents)==4 else "FAIL")
if __name__=="__main__":
 EcosystemSync().sync()
