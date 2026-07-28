from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[2]

class CoderSrc:
    """Senior Dev Hands - writes production code"""

    def read_file(self, path: str):
        p = ROOT / path if not Path(path).is_absolute() else Path(path)
        if not p.exists():
            return f"FILE NOT FOUND: {p}"
        return p.read_text()[:10000]

    def write_file(self, path: str, content: str):
        p = ROOT / path if not Path(path).is_absolute() else Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)
        print(f"[CODER SRC] WROTE: {p} ({len(content)} chars)")
        return str(p)

    def edit_file(self, path: str, old: str, new: str):
        p = ROOT / path
        text = p.read_text()
        if old not in text:
            print(f"[CODER SRC] OLD string not found in {path}")
            return False
        p.write_text(text.replace(old, new, 1))
        print(f"[CODER SRC] EDITED: {path}")
        return True

    def create_feature(self, feature_name: str, spec: str):
        print(f"[CODER SRC] Creating feature: {feature_name} - {spec}")
        # template for new monkey or feature
        return self.write_file(f"features/{feature_name}.py", f'"""{spec}"""\n\ndef main():\n print("{feature_name} online")\n')
