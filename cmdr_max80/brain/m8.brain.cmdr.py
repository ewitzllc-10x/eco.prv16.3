from src_code.brain.code_analyzer import CodeAnalyzer
from src_code.dna.code_memory import CodeMemory
from src_code.dna.mcp_memory import MCPMemory
from src_code.workflow.logic_manager import LogicManager

class CmdrMax80:
    def __init__(self):
        self.brain = CodeAnalyzer()
        self.ram = CodeMemory()
        self.mcp = MCPMemory()
        print("[cmdr_max80] Booted | RAM + MCP:9749")

    def process(self, code, key="last"):
        a = self.brain.analyze(code)
        self.ram.remember(key, a)
        self.mcp.remember(key, a)
        print(f"[MEM] {key} -> RAM + MCP")
        return a

    def recall(self, key):
        v = self.ram.recall(key) or self.mcp.recall(key)
        print(f"[RECALL] {key} -> {v}")
        return v

def main():
    c = CmdrMax80()
    c.process("print('boot')", "boot_test")
    c.recall("boot_test")

if __name__ == "__main__":
    main()
