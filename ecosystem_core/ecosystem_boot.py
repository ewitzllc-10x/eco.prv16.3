import json
import os
from pathlib import Path

BASE = Path(__file__).resolve().parent
print("[BOOT] v1.6.3 pro16v3erbs - adm(10)->max80(9.5)->cpt(9)->1lt(8)")

# Load readiness
with open(BASE / "readiness.json") as f:
    readiness = json.load(f)
print(f"[READINESS] {readiness['validation']['exact_chain']}")

# Load registry
with open(BASE / "agent_registry.json") as f:
    registry = json.load(f)
print(f"[REGISTRY] Agents: {list(registry.keys()) if isinstance(registry, dict) else registry}")

# Load protocol map
with open(BASE.parent / "protocols/protocol_map.json") as f:
    pmap = json.load(f)
print(f"[PROTOCOLS] {list(pmap.get('protocols', {}).keys())}")

# Import your executor
from protocol_executor import ProtocolExecutor
ex = ProtocolExecutor()
for proto in ["core.init", "core.boot", "core.sync"]:
    try:
        r = ex.execute(proto)
        print(f"[EXEC] {proto} -> {r['status']}")
    except Exception as e:
        print(f"[EXEC] {proto} FAIL: {e}")

print("[BOOT] OPERATIONAL")
