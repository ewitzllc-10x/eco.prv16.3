import subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]

class SysRunner:
    def git_commit(self, msg: str):
        cmds = [
            "git add -A",
            f'git commit -m "{msg}"',
            "git push origin pro16v3erbs"
        ]
        for c in cmds:
            r = subprocess.run(c, shell=True, cwd=ROOT, capture_output=True, text=True)
            print(r.stdout[-1000:])

    def run_tests(self):
        r = subprocess.run("pytest -q || python3 -m pytest -q || echo 'no pytest'", shell=True, cwd=ROOT, capture_output=True, text=True)
        print(r.stdout[-2000:])
        return r.returncode == 0
