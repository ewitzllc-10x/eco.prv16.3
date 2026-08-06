from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
class Lt1CoderBrain:
    def think(self, task): return f"[1LT ACTION CODER] Executing: {task}"
    def plan(self, task): return ["EXECUTE", "CODE", "TEST", "REPORT to CPT"]
