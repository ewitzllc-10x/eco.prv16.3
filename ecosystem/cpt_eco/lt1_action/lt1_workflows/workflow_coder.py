from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from cpt_eco.lt1_action.lt1_brain.brain_coder import Lt1CoderBrain
from cpt_eco.lt1_action.lt1_src.src_coder import Lt1SrcCoder

class Lt1WorkflowCoder:
    def __init__(self):
        self.brain = Lt1CoderBrain()
        self.coder = Lt1SrcCoder()
        print("[1LT ACTION] SENIOR CODER BOOTED - Execution Engine")
    def execute(self, order):
        print(f"[1LT ACTION] {self.brain.think(order)}")
        return f"1LT CODER: {order}"

if __name__ == "__main__":
    Lt1WorkflowCoder().execute("Execute Stallion feature")
