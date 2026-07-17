import os
import json
import time

class EcosystemMonitor:
    def __init__(self):
        self.base = os.path.dirname(__file__)

        # Load core modules
        self.stability = self.load_json("stability.json")
        self.readiness = self.load_json("readiness.json")
        self.communication = self.load_json("communication_flow.json")
        self.cycles = self.load_json("cycles.json")

        # Monitoring log
        self.log_entries = []

    # ---------------------------------------------------------
    # JSON LOADING
    # ---------------------------------------------------------
    def load_json(self, filename):
        path = os.path.join(self.base, filename)
        with open(path, "r") as f:
            return json.load(f)

    # ---------------------------------------------------------
    # LOGGING
    # ---------------------------------------------------------
    def log(self, message):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[MONITOR::{timestamp}] {message}"
        self.log_entries.append(entry)
        print(entry)

    # ---------------------------------------------------------
    # STABILITY MONITORING
    # ---------------------------------------------------------
    def monitor_stability(self):
        core = self.stability["stability_core"]

        if not core["ecosystem_must_be_stable"]:
            self.log("❌ Stability violation detected.")
            return False

        self.log("✔ Stability OK.")
        return True

    # ---------------------------------------------------------
    # READINESS MONITORING
    # ---------------------------------------------------------
    def monitor_readiness(self):
        criteria = self.readiness["criteria"]

        for key, value in criteria.items():
            if not value:
                self.log(f"❌ Readiness violation: {key}")
                return False

        self.log("✔ Readiness OK.")
        return True

    # ---------------------------------------------------------
    # COMMUNICATION MONITORING
    # ---------------------------------------------------------
    def monitor_communication(self):
        channels = self.communication
