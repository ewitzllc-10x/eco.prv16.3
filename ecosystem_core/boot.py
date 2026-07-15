import os
import json
import time

from agent_loader import AgentLoader
from task_router import TaskRouter

class EcosystemBoot:
    def __init__(self):
        self.base = os.path.dirname(__file__)
        self.core = self.load_json("ecosystem_core.json")
        self.stability = self.load_json("stability.json")
        self.readiness = self.load_json("readiness.json")

        self.loader = AgentLoader()
        self.router = TaskRouter()

        self.boot_log = []

    def load_json(self, filename):
        path = os.path.join(self.base, filename)
        with open(path, "r") as f:
            return json.load(f)

    def log(self, message):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[BOOT::{timestamp}] {message}"
        self.boot_log.append(entry)
        print(entry)

    def verify_core(self):
        self.log("Verifying ecosystem core integrity...")
        required = self.core["requirements"]
        for key, value in required.items():
            if not value:
                self.log(f"Core requirement failed: {key}")
                return False
        self.log("Core integrity verified.")
        return True

    def verify_stability(self):
        self.log("Running stability verification...")
        if not self.stability["stability_core"]["ecosystem_must_be_stable"]:
            self.log("Stability requirement failed.")
            return False
        self.log("Stability confirmed.")
        return True

    def verify_readiness(self):
        self.log("Checking readiness criteria...")
        criteria = self.readiness["criteria"]
        for key, value in criteria.items():
            if not value:
                self.log(f"Readiness failure: {key}")
                return False
        self.log("Ecosystem readiness confirmed.")
        return True

    def load_agents(self):
        self.log("Discovering agents...")
        discovered = self.loader.discover_agents()
        self.log(f"Agents found: {discovered}")
        self.log("Loading agents...")
        results = self.loader.load_all_agents()
        for r in results:
            self.log(r)
        return True

    def boot(self):
        self.log("=== Ecosystem Boot Sequence Initiated ===")
        if not self.verify_core():
            self.log("Boot aborted: core verification failed.")
            return False
        if not self.verify_stability():
            self.log("Boot aborted: stability verification failed.")
            return False
        if not self.verify_readiness():
            self.log("Boot aborted: readiness verification failed.")
            return False
        self.load_agents()
        self.log("Ecosystem successfully booted.")
        self.log("System is now operational.")
        return True

if __name__ == "__main__":
    boot = EcosystemBoot()
    boot.boot()
