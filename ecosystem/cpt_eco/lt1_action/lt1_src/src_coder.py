from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
class Lt1SrcCoder:
    def write(self, path, content):
        p = ROOT / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)
        print(f"[1LT ACTION] WROTE {path}")
        return str(p)
