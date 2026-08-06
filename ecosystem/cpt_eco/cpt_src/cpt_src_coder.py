from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
class CptSrcCoder:
    def write(self, path, content):
        p = ROOT / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)
        print(f"[CPT ECO CODER] WROTE {path}")
        return str(p)
    def read(self, path):
        return (ROOT / path).read_text()[:5000] if (ROOT / path).exists() else "NOT FOUND"
