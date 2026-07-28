from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
class Lt2SrcCoder:
    def write(self, path, content):
        p = ROOT / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)
        print(f"[2LT DEVIL DOG] WROTE {path}")
        return str(p)
