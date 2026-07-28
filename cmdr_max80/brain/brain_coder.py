import ast, pathlib, subprocess, json, traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1].parents[0] # eco.prv16.3 root

class CoderBrain:
    """Senior Dev Brain - thinks like Staff Engineer"""

    def analyze_repo(self, target="."):
        files = list(ROOT.rglob("*.py"))
        # ignore venv/cache
        files = [f for f in files if "agentenv" not in str(f) and "__pycache__" not in str(f)]
        return {"total_py_files": len(files), "files": [str(f.relative_to(ROOT)) for f in files[:50]]}

    def plan_task(self, task: str):
        print(f"[CODER BRAIN] Planning: {task}")
        return {
            "task": task,
            "steps": ["READ relevant files", "DESIGN solution", "CODE", "TEST", "DEBUG loop", "COMMIT"],
            "strategy": "minimal, production-ready, no placeholders"
        }

    def analyze_error(self, error_log: str):
        print(f"[CODER BRAIN] Debugging error...")
        # Simple senior dev heuristic
        if "ModuleNotFoundError" in error_log: return "Missing import - check path or pip"
        if "SyntaxError" in error_log: return "Syntax error - check AST"
        if "FileNotFoundError" in error_log: return "Wrong file path - check ROOT"
        return "General error - read traceback bottom-up"
