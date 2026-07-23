import os, json, pathlib, ast
ROOT = pathlib.Path(".")
# your claimed infra
EXPECTED = """
Max80/ecosystem_core/identity.json
Max80/ecosystem_core/hierarchy.json
Max80/ecosystem_core/communication.json
Max80/ecosystem_core/cycles.json
Max80/ecosystem_core/stability.json
Max80/ecosystem_core/readiness.json
Max80/ecosystem_core/cpt_eco/adm_ewitz/identity.json
Max80/ecosystem_core/cpt_eco/adm_ewitz/authority.json
Max80/ecosystem_core/cpt_eco/adm_ewitz/duties.json
Max80/ecosystem_core/cpt_eco/adm_ewitz/routing.json
Max80/ecosystem_core/cpt_eco/adm_ewitz/command_paths.json
Max80/ecosystem_core/cpt_eco/adm_ewitz/stability.json
Max80/ecosystem_core/cpt_eco/adm_ewitz/history.json
Max80/ecosystem_core/cpt_eco/1lt_act.json
Max80/ecosystem_core/cpt_eco/2lt_act.json
Max80/ecosystem_core/cpt_eco/governance.json
Max80/ecosystem_core/cpt_eco/authority.json
Max80/ecosystem_core/cpt_eco/stability.json
Max80/ecosystem_core/cpt_eco/protocol_map.json
Max80/ecosystem_core/cpt_eco/routing_rules.json
Max80/ecosystem_core/cpt_eco/ecosystem_rules.json
Max80/ecosystem_core/knowledge/glossary.json
Max80/ecosystem_core/knowledge/topics.json
Max80/ecosystem_core/knowledge/rules.json
Max80/ecosystem_core/knowledge/processes.json
Max80/ecosystem_core/knowledge/decisions.json
Max80/ecosystem_core/knowledge/history.json
Max80/ecosystem_core/agents/lieutenants/1lt/identity.json
Max80/ecosystem_core/agents/lieutenants/1lt/duties.json
Max80/ecosystem_core/agents/lieutenants/1lt/routing.json
Max80/ecosystem_core/agents/lieutenants/1lt/authority.json
Max80/ecosystem_core/agents/lieutenants/2lt/identity.json
Max80/ecosystem_core/agents/lieutenants/2lt/duties.json
Max80/ecosystem_core/agents/lieutenants/2lt/routing.json
Max80/ecosystem_core/agents/lieutenants/2lt/authority.json
Max80/ecosystem_core/agents/governors/identity.json
Max80/ecosystem_core/agents/governors/duties.json
Max80/ecosystem_core/agents/governors/authority.json
Max80/ecosystem_core/agents/workers/identity.json
Max80/ecosystem_core/agents/workers/tasks.json
Max80/ecosystem_core/agents/workers/routing.json
Max80/ecosystem_core/protocols/commander_protocol.json
Max80/ecosystem_core/protocols/routing_rules.json
Max80/ecosystem_core/protocols/protocol_map.json
Max80/ecosystem_core/governance/authority.json
Max80/ecosystem_core/governance/stability.json
Max80/ecosystem_core/governance/governance_rules.json
Max80/ecosystem_core/systems/ecosystem_sync.py
Max80/ecosystem_core/systems/report_engine.py
Max80/ecosystem_core/systems/protocol_executor.py
Max80/ecosystem_core/systems/subsystem_init.py
Max80/frontend/index.html
Max80/frontend/styles.css
Max80/frontend/app.js
Max80/backend/server.py
Max80/backend/api/routes.py
Max80/backend/api/handlers.py
Max80/backend/api/models.py
Max80/websocket/ws_server.py
Max80/websocket/ws_routes.py
Max80/intelligence/ai_core.py
Max80/intelligence/agent_router.py
Max80/intelligence/decision_engine.py
Max80/intelligence/memory_core.json
ecosystem/cmdr_max80/cmdr_max80.py
ecosystem/cmdr_max80/sync_max80/os_max80.py
ecosystem/cmdr_max80/src_code/brain/code_analyzer.py
""".strip().splitlines()

blue = 0
red = 0
for rel in EXPECTED:
    p = ROOT / rel.strip()
    exists = p.exists()
    ok = False
    reason = ""
    if not exists:
        reason = "MISSING"
    else:
        if p.suffix == ".json":
            try:
                json.load(open(p))
                ok = p.stat().st_size > 5
                reason = f"OK {p.stat().st_size}b" if ok else "EMPTY"
            except Exception as e:
                reason = f"BAD JSON: {e}"
        elif p.suffix == ".py":
            try:
                ast.parse(open(p).read())
                ok = True
                reason = f"OK {p.stat().st_size}b"
            except Exception as e:
                reason = f"SYNTAX ERR: {e}"
        else:
            ok = p.stat().st_size > 0
            reason = f"OK {p.stat().st_size}b"

    icon = "🔵" if ok and exists else "🔴"
    if icon == "🔵": blue += 1
    else: red += 1
    print(f"{icon} {rel:<70} {reason}")

print(f"\nTOTAL: {blue} 🔵 DONE / {blue+red} | {red} 🔴 TODO | {blue/(blue+red)*100:.1f}%")
