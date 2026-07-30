import time, json, importlib.util, sys
from pathlib import Path

ROOT = Path.home() / "eco.prv16.3"
sys.path.insert(0, str(ROOT))

class AutMax80:
    def __init__(self):
        self.rank = "CMDR_MAX80"
        self.status = "AUT_MAX80_DELEGATION_ACTIVE"
        self.queue = ROOT / "adm_ewitz" / "orders.json"
        self.queue.parent.mkdir(parents=True, exist_ok=True)
        if not self.queue.exists():
            self.queue.write_text("[]")
        print("[AUT_MAX80] BOOTED - DELEGATION MODE")
        print(f"[AUT_MAX80] Queue: {self.queue}")

    def check_orders(self):
        """Pull orders from Admiral"""
        try:
            data = json.loads(self.queue.read_text())
            if data:
                print(f"[AUT_MAX80] Found {len(data)} order(s)")
                self.queue.write_text("[]")
                return data
        except Exception as e:
            print(f"[AUT_MAX80] Queue read error: {e}")
        # Also scan adm_ewitz/*.md modified in last 2min
        for f in (ROOT / "adm_ewitz").rglob("*.md"):
            try:
                if f.stat().st_mtime > time.time() - 120:
                    txt = f.read_text()[:500]
                    if "ORDER:" in txt or "MISSION:" in txt:
                        print(f"[AUT_MAX80] Order found in {f}")
                        return [txt]
            except: pass
        return []

    def delegate_to_cpt(self, order):
        """Delegate to CPT_ECO - SAFE MODE"""
        print(f"[CMDR -> CPT_ECO] Delegating: {order[:80]}...")
        try:
            # Find CPT entry
            cpt_main = ROOT / "cpt_eco" / "cpt_src" / "cpt_src.cmdr_link.py"
            cpt_entry = ROOT / "cpt_eco" / "cpt_eco.py"

            if cpt_main.exists():
                print(f"[CMDR] Found link: {cpt_main}")
                spec = importlib.util.spec_from_file_location("cpt_link", str(cpt_main))
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                if hasattr(mod, 'execute'):
                    return mod.execute(order)

            # Fallback - log for CPT to pick up
            mission_file = ROOT / "cpt_eco" / "mission.json"
            mission_file.write_text(json.dumps({"from":"CMDR_MAX80","order":order,"ts":time.time()}, indent=2))
            print(f"[CMDR] Mission dropped to {mission_file} for CPT_ECO pickup")
            return "DELEGATED_TO_CPT_FILE"

        except Exception as e:
            print(f"[CMDR->CPT] Delegation error: {e}")
            import traceback; traceback.print_exc()
            return None

    def run(self):
        print("[AUT_MAX80] DELEGATION LOOP STARTED - 15s cycle")
        while True:
            try:
                orders = self.check_orders()
                for order in orders:
                    result = self.delegate_to_cpt(order)
                    log = ROOT / "logs" / "aut_max80.log"
                    log.parent.mkdir(exist_ok=True)
                    with open(log, "a") as lf:
                        lf.write(f"{time.ctime()} | ORDER: {str(order)[:100]} | RESULT: {result}\n")
                time.sleep(15)
            except KeyboardInterrupt:
                print("[AUT_MAX80] SAFE SHUTDOWN")
                break
            except Exception as e:
                print(f"[AUT_MAX80] Loop error: {e}")
                time.sleep(5)

if __name__ == "__main__":
    AutMax80().run()
