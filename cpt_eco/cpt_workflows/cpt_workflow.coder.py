from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from cpt_eco.cpt_brain.cpt_brain_coder import CptCoderBrain
from cpt_eco.cpt_src.cpt_src_coder import CptSrcCoder
from cpt_eco.cpt_src.cpt_src_debugger import CptDebugger

class CptWorkflowCoder:
    def __init__(self):
        self.brain = CptCoderBrain()
        self.coder = CptSrcCoder()
        self.debug = CptDebugger()
        print("[CPT ECO] SENIOR CODER BOOTED - Eco Architect")
    def execute(self, order):
        print(f"[CPT ECO] {order} | {self.brain.think(order)}")
        print(f"[CPT ECO] Repo: {self.brain.analyze_repo()['total']} files")
        return f"CPT ECO CODER: {order}"

if __name__ == "__main__":
    CptWorkflowCoder().execute("Build Eco ecosystem")
