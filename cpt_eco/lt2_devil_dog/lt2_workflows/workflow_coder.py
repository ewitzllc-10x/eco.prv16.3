from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from cpt_eco.lt2_devil_dog.lt2_brain.brain_coder import Lt2CoderBrain
from cpt_eco.lt2_devil_dog.lt2_src.src_coder import Lt2SrcCoder

class Lt2WorkflowCoder:
    def __init__(self):
        self.brain = Lt2CoderBrain()
        self.coder = Lt2SrcCoder()
        print("[2LT DEVIL DOG] SENIOR CODER BOOTED - Grunt Coder / Debugger")
    def execute(self, order):
        print(f"[2LT DEVIL] {self.brain.think(order)}")
        return f"2LT CODER: {order}"

if __name__ == "__main__":
    Lt2WorkflowCoder().execute("Grunt build Stallion checkout")
