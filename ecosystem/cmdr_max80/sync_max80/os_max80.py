import sys
from pathlib import Path

# auto find src_code by walking up
cur = Path(__file__).resolve()
for parent in [cur.parent, *cur.parents]:
    if (parent / "src_code").exists():
        sys.path.insert(0, str(parent))
        print(f"[PATH] root found: {parent}")
        break
    if (parent / "ecosystem" / "cmdr_max80" / "src_code").exists():
        sys.path.insert(0, str(parent / "ecosystem" / "cmdr_max80"))
        print(f"[PATH] root found: {parent / 'ecosystem' / 'cmdr_max80'}")
        break

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
        print(f"[os_max80] Booted | {ROOT} | RAM + MCP:9749 | path=cmdr_max80/sync_max80/os_max80.py")

    def process(self, code, key="last"):
        a = self.brain.analyze(code)
        self.ram.remember(key, a)
        self.mcp.remember(key, a)
        print(f"[MEM] {key} -> RAM + MCP")
        return a

if __name__ == "__main__":
    OsMax80()
