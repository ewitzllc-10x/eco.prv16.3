import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
class CptDebugger:
    def run(self, cmd):
        r = subprocess.run(cmd, shell=True, cwd=ROOT, capture_output=True, text=True)
        print(r.stdout[-1500:])
        if r.stderr: print(r.stderr[-1500:])
        return r.returncode == 0
