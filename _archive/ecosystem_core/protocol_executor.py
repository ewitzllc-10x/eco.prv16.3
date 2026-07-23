import os
import json
import importlib.util
import time
import traceback
from pathlib import Path

class ProtocolExecutor:
    def __init__(self):
        # Resolve from ecosystem_core or protocols folder
        self.base = Path(__file__).resolve().parent
        # Try both locations
        for p in [self.base / "../protocols/protocol_map.json",
                  self.base / "protocol_map.json",
                  Path.home() / "pro16v3erbs/protocols/protocol_map.json",
                  Path.home() / "eco.prv16.3/protocols/protocol_map.json"]:
            if p.exists():
                with open(p, "r") as f:
                    self.protocol_map = json.load(f)
                break
        else:
            raise FileNotFoundError("protocol_map.json not found")

        self.exec_log = []

    def log(self, message, level="INFO"):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[EXEC::{level}::{timestamp}] {message}"
        self.exec_log.append(entry)
        print(entry)

    def validate_protocol(self, protocol):
        if protocol not in self.protocol_map.get("protocols", {}):
            self.log(f"❌ Unknown protocol: {protocol}", "ERROR")
            return None
        info = self.protocol_map["protocols"][protocol]
        if not all(k in info and info[k] for k in ["destination", "script", "class"]):
            self.log(f"❌ Protocol incomplete: {protocol} -> {info}", "ERROR")
            return None
        return info

    def load_module(self, script_path: Path, class_name):
        try:
            spec = importlib.util.spec_from_file_location(class_name, str(script_path))
            if spec is None or spec.loader is None:
                self.log(f"❌ Spec failed: {script_path}", "ERROR")
                return None
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        except Exception as e:
            self.log(f"❌ Load failed {script_path}: {e}\n{traceback.format_exc()}", "ERROR")
            return None

        if not hasattr(module, class_name):
            self.log(f"❌ Class {class_name} not found in {script_path}", "ERROR")
            return None
        return getattr(module, class_name)

    def execute(self, protocol, intent=None, method_hint=None):
        self.log(f"Executing protocol: {protocol} | intent={intent}")
        info = self.validate_protocol(protocol)
        if info is None:
            return {"status": "error", "reason": "invalid_protocol", "protocol": protocol}

        # Build absolute path
        dest = Path(info["destination"])
        if not dest.is_absolute():
            # destination is like "ecosystem_core" or "../ecosystem_core"
            script_path = (self.base / dest / info["script"]).resolve()
        else:
            script_path = dest / info["script"]

        if not script_path.exists():
            # Fallback search in both repos
            for base in [Path.home() / "pro16v3erbs", Path.home() / "eco.prv16.3", self.base.parent]:
                alt = base / info["destination"] / info["script"]
                if alt.exists():
                    script_path = alt
                    break
            else:
                self.log(f"❌ Script missing: {script_path}", "ERROR")
                return {"status": "error", "reason": "missing_script", "protocol": protocol, "path": str(script_path)}

        cls = self.load_module(script_path, info["class"])
        if cls is None:
            return {"status": "error", "reason": "class_not_found", "protocol": protocol}

        try:
            instance = cls()
            # Priority: method_hint > intent > boot > sync > generate_report > execute > run
            for m in [method_hint, intent, "boot", "sync", "generate_report", "execute", "run", "handle"]:
                if m and hasattr(instance, m) and callable(getattr(instance, m)):
                    self.log(f"→ Calling {info['class']}.{m}()")
                    result = getattr(instance, m)()
                    self.log(f"✔ Protocol executed: {protocol}")
                    return {"status": "success", "protocol": protocol, "method": m, "result": result}

            self.log(f"❌ No executable method in {info['class']}", "ERROR")
            return {"status": "error", "reason": "no_executable_method", "protocol": protocol}
        except Exception as e:
            self.log(f"❌ Exec error {protocol}: {e}\n{traceback.format_exc()}", "ERROR")
            return {"status": "error", "reason": "exception", "protocol": protocol, "error": str(e)}

if __name__ == "__main__":
    executor = ProtocolExecutor()
    print(executor.execute("core.init"))
    print(executor.execute("core.boot"))
    print(executor.execute("core.sync"))
