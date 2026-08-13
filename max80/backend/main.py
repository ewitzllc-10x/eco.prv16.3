from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Max80 Heart - cmdr max80")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 100 AGENTS UNDER CMDR MAX80
agents = {
    i: {"id": i, "status": "idle", "task": f"Ready for cmdr max80", "logs": "Standing by", "commander": "cmdr max80"}
    for i in range(1, 101)
}

@app.get("/health")
def health():
    return {"status": "HEART BEATING", "commander": "cmdr max80", "agents": 100}

@app.get("/api/agents")
def list_agents():
    return list(agents.values())

@app.post("/api/agents/{agent_id}/toggle")
def toggle_agent(agent_id: int):
    a = agents.get(agent_id)
    if not a: return {"error": "not found"}
    a["status"] = "running" if a["status"] == "idle" else "idle"
    a["task"] = f"Executing under cmdr max80" if a["status"] == "running" else "Idle"
    return a

@app.post("/api/agents/start-all")
def start_all():
    for a in agents.values():
        a["status"] = "running"
        a["task"] = "All 100 running under cmdr max80"
    return {"started": 100}

@app.post("/api/agents/stop-all")
def stop_all():
    for a in agents.values():
        a["status"] = "idle"
        a["task"] = "Stopped by cmdr max80"
    return {"stopped": 100}
