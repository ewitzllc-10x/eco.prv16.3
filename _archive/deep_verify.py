import json, ast
from pathlib import Path
ROOT=Path(".")
EXPECTED = [
"Max80/ecosystem_core/identity.json",
"Max80/ecosystem_core/hierarchy.json",
"Max80/ecosystem_core/communication.json",
"Max80/ecosystem_core/cycles.json",
"Max80/ecosystem_core/stability.json",
"Max80/ecosystem_core/readiness.json",
"Max80/ecosystem_core/cpt_eco/adm_ewitz/identity.json",
"Max80/ecosystem_core/cpt_eco/adm_ewitz/authority.json",
"Max80/ecosystem_core/cpt_eco/adm_ewitz/duties.json",
"Max80/ecosystem_core/cpt_eco/adm_ewitz/routing.json",
"Max80/ecosystem_core/cpt_eco/adm_ewitz/command_paths.json",
"Max80/ecosystem_core/cpt_eco/adm_ewitz/stability.json",
"Max80/ecosystem_core/cpt_eco/adm_ewitz/history.json",
"Max80/ecosystem_core/cpt_eco/1lt_act.json",
"Max80/ecosystem_core/cpt_eco/2lt_act.json",
"Max80/ecosystem_core/cpt_eco/governance.json",
"Max80/ecosystem_core/cpt_eco/authority.json",
"Max80/ecosystem_core/cpt_eco/stability.json",
"Max80/ecosystem_core/cpt_eco/protocol_map.json",
"Max80/ecosystem_core/cpt_eco/routing_rules.json",
"Max80/ecosystem_core/cpt_eco/ecosystem_rules.json",
"Max80/ecosystem_core/knowledge/glossary.json",
"Max80/ecosystem_core/knowledge/topics.json",
"Max80/ecosystem_core/knowledge/rules.json",
"Max80/ecosystem_core/knowledge/processes.json",
"Max80/ecosystem_core/knowledge/decisions.json",
"Max80/ecosystem_core/knowledge/history.json",
"Max80/ecosystem_core/agents/lieutenants/1lt/identity.json",
"Max80/ecosystem_core/agents/lieutenants/1lt/duties.json",
"Max80/ecosystem_core/agents/lieutenants/1lt/routing.json",
"Max80/ecosystem_core/agents/lieutenants/1lt/authority.json",
"Max80/ecosystem_core/agents/lieutenants/2lt/identity.json",
"Max80/ecosystem_core/agents/lieutenants/2lt/duties.json",
"Max80/ecosystem_core/agents/lieutenants/2lt/routing.json",
"Max80/ecosystem_core/agents/lieutenants/2lt/authority.json",
"Max80/ecosystem_core/agents/governors/identity.json",
"Max80/ecosystem_core/agents/governors/duties.json",
"Max80/ecosystem_core/agents/governors/authority.json",
"Max80/ecosystem_core/agents/workers/identity.json",
"Max80/ecosystem_core/agents/workers/tasks.json",
"Max80/ecosystem_core/agents/workers/routing.json",
"Max80/ecosystem_core/protocols/commander_protocol.json",
"Max80/ecosystem_core/protocols/routing_rules.json",
"Max80/ecosystem_core/protocols/protocol_map.json",
"Max80/ecosystem_core/governance/authority.json",
"Max80/ecosystem_core/governance/stability.json",
"Max80/ecosystem_core/governance/governance_rules.json",
"Max80/ecosystem_core/systems/ecosystem_sync.py",
"Max80/ecosystem_core/systems/report_engine.py",
"Max80/ecosystem_core/systems/protocol_executor.py",
"Max80/ecosystem_core/systems/subsystem_init.py",
"Max80/frontend/index.html",
"Max80/frontend/styles.css",
"Max80/frontend/app.js",
"Max80/backend/server.py",
"Max80/backend/api/routes.py",
"Max80/backend/api/handlers.py",
"Max80/backend/api/models.py",
"Max80/websocket/ws_server.py",
"Max80/websocket/ws_routes.py",
"Max80/intelligence/ai_core.py",
"Max80/intelligence/agent_router.py",
"Max80/intelligence/decision_engine.py",
"Max80/intelligence/memory_core.json",
]

print("=== REAL DISK STRUCTURE ===")
actual = sorted([str(p) for p in ROOT.rglob("*") if p.is_file() and "Max80" in str(p)])
for f in actual[:200]:
    print(f)

print("\n=== PLACEMENT CHECK ===")
ok_count=0
for rel in EXPECTED:
    p=ROOT/rel
    if not p.exists():
        print(f"🔴 MISSING: {rel}")
        continue
    # check case sensitive placement
    if str(p) != rel and not str(p).startswith("./"):
        # Path object keeps case
        pass
    if p.suffix==".json":
        try:
            data=json.loads(p.read_text())
            if not data:
                print(f"🟡 EMPTY JSON: {rel}")
            else:
                print(f"🔵 OK JSON: {rel} | keys={list(data.keys())[:3]}")
                ok_count+=1
        except Exception as e:
            print(f"🔴 BAD JSON: {rel} -> {e}")
    elif p.suffix==".py":
        try:
            ast.parse(p.read_text())
            print(f"🔵 OK PY: {rel} | {p.stat().st_size}b")
            ok_count+=1
        except Exception as e:
            print(f"🔴 BAD PY: {rel} -> {e}")
    else:
        print(f"🔵 OK FILE: {rel} | {p.stat().st_size}b")
        ok_count+=1

print(f"\nTOTAL VERIFIED: {ok_count}/{len(EXPECTED)} = {ok_count/len(EXPECTED)*100:.1f}%")
if ok_count==len(EXPECTED):
    print("💯 100% REAL - ALL PROPERLY PLACED AND VALID")
else:
    print("⚠️  NOT 100% - FIX REDS ABOVE")
