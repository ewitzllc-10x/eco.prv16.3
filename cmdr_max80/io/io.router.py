from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

class CmdrIoRouter:
    def route(self, cmd):
        print(f"[CMDR MAX80 IO] Right hand routing for Admiral: {cmd}")
        if any(k in cmd.lower() for k in ["build", "code", "fix", "debug", "stallion"]):
            print(f"[CMDR IO] -> CODER PIPELINE")
        return f"CMDR ROUTED: {cmd}"

    def code(self, path, content):
        from cmdr_max80.src.src_coder import CoderSrc
        return CoderSrc().write_file(path, content)
