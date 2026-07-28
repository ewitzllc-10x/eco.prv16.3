import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

class CoderDebugger:
    """Senior Dev Debugger - fixes until green"""

    def run(self, cmd: str):
        print(f"[DEBUGGER] RUN: {cmd}")
        result = subprocess.run(cmd, shell=True, cwd=ROOT, capture_output=True, text=True)
        print(result.stdout[-2000:] if result.stdout else "")
        if result.stderr:
            print(f"[ERR]\n{result.stderr[-2000:]}")
        return result

    def test_file(self, path: str):
        return self.run(f"{sys.executable} {path}")

    def debug_loop(self, file_path: str, max_retries=3):
        for i in range(max_retries):
            res = self.test_file(file_path)
            if res.returncode == 0:
                print(f"[DEBUGGER] FIXED in {i} tries - {file_path} GREEN")
                return True
            print(f"[DEBUGGER] Attempt {i+1}/{max_retries} failed, analyzing...")
            # Here senior dev would auto-patch - for now report
        return False
