from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]

class CptCoderBrain:
    def think(self, task: str):
        return f"[CPT ECO CODER] Architecting: {task}"
    def plan(self, task):
        return ["ANALYZE eco", "DESIGN system", "DELEGATE to LTs", "CODE core", "TEST chain"]
    def analyze_repo(self):
        files = list(ROOT.rglob("*.py"))
        files = [f for f in files if "agentenv" not in str(f) and "__pycache__" not in str(f)]
        return {"total": len(files)}
