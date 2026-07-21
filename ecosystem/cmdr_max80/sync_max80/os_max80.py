import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src_code.brain.code_analyzer import CodeAnalyzer
from src_code.dna.code_memory import CodeMemory
from src_code.dna.mcp_memory import MCPMemory
from src_code.workflow.logic_manager import LogicManager

ROOT = "eco.prv16.3"

class OsMax80:
    def __init__(self):
        self.brain = CodeAnalyzer()
        self.ram = CodeMemory()
        self.mcp = MCPMemory()
        self.logic = LogicManager()
        print(f"[os_max80] Booted | {ROOT} | path=cmdr_max80/sync_max80/os_max80.py")

    def process(self, code, key="last"):
        a = self.brain.analyze(code)
        self.ram.remember(key, a)
        self.mcp.remember(key, a)
        return a

if __name__ == "__main__":
    OsMax80()
