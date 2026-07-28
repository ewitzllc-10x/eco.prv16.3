from cmdr_max80.brain.brain_coder import CoderBrain
from cmdr_max80.src.src_coder import CoderSrc
from cmdr_max80.src.src_debugger import CoderDebugger
from cmdr_max80.systems.sys_runner import SysRunner

class CmdrWorkflow:
    def __init__(self):
        self.brain = CoderBrain()
        self.coder = CoderSrc()
        self.debugger = CoderDebugger()
        self.runner = SysRunner()
        print("[CMDR MAX80] SENIOR CODER BOOTED - Ready to code, debug, push")

    def execute(self, cmd):
        print(f"\n[CMDR MAX80] Right hand executing for Admiral: {cmd}\n")
        plan = self.brain.plan_task(cmd)
        repo = self.brain.analyze_repo()
        print(f"[PLAN] {plan['steps']}")
        print(f"[REPO] {repo['total_py_files']} py files")
        if any(k in cmd.lower() for k in ["build", "stallion", "website"]):
            # PROVE IT - build Stallion MVP
            self.coder.write_file("stallion_website/index.html", "<h1>STALLION 10X - BUILT BY CMDR MAX80</h1><p>Admiral Ewitz top table online</p>")
            print("[CMDR] STALLION WEBSITE BUILT")
        return f"CMDR: MAX80 SENIOR CODER EXECUTED - {cmd}"

    def code_file(self, path, content):
        return self.coder.write_file(path, content)
    def debug_file(self, path):
        return self.debugger.debug_loop(path)
    def commit(self, msg):
        return self.runner.git_commit(msg)
