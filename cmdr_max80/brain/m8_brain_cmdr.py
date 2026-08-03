# & replaced with fake
class CodeAnalyzer:
    def analyze(self, code): return f"FAKE_ANALYSIS:{len(code)}chars"
class CodeMemory:
    def remember(self, key, val): pass
class MCPMemory:
    def remember(self, key, val): pass
class CodeAnalyzer:
    def analyze(self, code): return f"FAKE_ANALYSIS:{len(code)}chars"
# & replaced with fake
class CodeAnalyzer:
    def analyze(self, code): return f"FAKE_ANALYSIS:{len(code)}chars"
class CodeMemory:
    def remember(self, key, val): pass
class MCPMemory:
    def remember(self, key, val): pass
# & replaced with fake
class CodeAnalyzer:
    def analyze(self, code): return f"FAKE_ANALYSIS:{len(code)}chars"
class CodeMemory:
    def remember(self, key, val): pass
class MCPMemory:
    def remember(self, key, val): pass
# & replaced with fake
class CodeAnalyzer:
    def analyze(self, code): return f"FAKE_ANALYSIS:{len(code)}chars"
class CodeMemory:
    def remember(self, key, val): pass
class MCPMemory:
    def remember(self, key, val): pass
from vault.memory import log_memory

class CmdrMax80:
    def __init__(self):
        self.db_path = "vault/eco_memory.db"
        self.brain = CodeAnalyzer()
        self.ram = CodeMemory()
        self.vault = log_memory
        self.mcp = MCPMemory()
        print("[cmdr_max80] Booted | RAM + MCP:9749")

    def recall(self, key):
        import sqlite3
        con = sqlite3.connect("vault/eco_memory.db")
        cur = con.cursor()
        cur.execute("SELECT data FROM memory WHERE data LIKE? ORDER BY ts DESC LIMIT 1", (f"%{key}%",))
        row = cur.fetchone()
        con.close()
        return row[0] if row else "No memory found"

    def list_memories(self):
        """LIST: Show all memories CMDR has saved."""
        import sqlite3
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        cur.execute("SELECT data, ts FROM memory ORDER BY ts DESC")
        rows = cur.fetchall()
        con.close()
        print(f"[CMDR] Found {len(rows)} memories:")
        for data, ts in rows[:10]:  # Show last 10
            print(f"  {ts} | {data[:60]}...")
        return rows

    def forget(self, key):
        """DELETE: Remove memories matching key."""
        import sqlite3
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        cur.execute("DELETE FROM memory WHERE data LIKE?", (f"%{key}%",))
        deleted = cur.rowcount
        con.commit()
        con.close()
        print(f"[CMDR] Forgot {deleted} memories matching: {key}")
        return deleted
    def process(self, code, key="last"):
        cached = self.recall(key)
        if cached != "No memory found":
            print(f"[CACHE] {key} -> recalled from vault")
            return cached
        a = self.brain.analyze(code)
        self.ram.remember(key, a)
        self.mcp.remember(key, a)
        print(f"[MEM] {key} -> RAM + MCP")
        self.vault("cmdr_max80", "memory", f"Processed {key} | analysis: {str(a)[:80]}")
        return a

