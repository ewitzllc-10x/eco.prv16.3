from divisions.base_division import BaseDivision

class ReconDivision(BaseDivision):
    def __init__(self, global_data):
        super().__init__("recon_division", global_data)

    def scan_area(self, payload):
        """Simulate recon scanning logic."""
        results = []

        if payload.get("terrain") == "urban":
            results.append("multiple vantage points identified")
        elif payload.get("terrain") == "forest":
            results.append("dense cover detected")
        elif payload.get("terrain") == "desert":
            results.append("open terrain, minimal cover")

        if payload.get("heat_signatures", 0) > 0:
            results.append(f"{payload['heat_signatures']} heat signatures detected")

        return results

    def detect_hostiles(self, payload):
        """Hostile detection logic."""
        hostiles = payload.get("hostiles", 0)

        if hostiles == 0:
            return "no_hostiles"
        elif hostiles <= 3:
            return "small_group"
        elif hostiles <= 10:
            return "medium_group"
        else:
            return "large_group"

    def recommend_action(self, terrain, hostiles):
        """Recommend next steps based on recon data."""
        if hostiles == "large_group":
            return "ops_division"
        if terrain == "forest" and hostiles == "medium_group":
            return "intel_division"
        if hostiles == "small_group":
            return "cmdr_max80"
        return "grunt_X"

    def process(self, packet):
        payload = packet["payload"]
        mission_id = packet["mission_id"]

        self.log(f"[RECON] Starting recon mission {mission_id}")

        # 1. Scan terrain
        scan_results = self.scan_area(payload)
        for r in scan_results:
            self.log(f"[RECON] Scan: {r}")

        # 2. Detect hostiles
        hostiles = self.detect_hostiles(payload)
        self.log(f"[RECON] Hostiles: {hostiles}")

        # 3. Recommend next action
        terrain = payload.get("terrain", "unknown")
        recommendation = self.recommend_action(terrain, hostiles)
        self.log(f"[RECON] Recommendation: {recommendation}")

        # 4. Final result
        summary = f"ReconDivision completed mission | terrain={terrain} | hostiles={hostiles} | recommended={recommendation}"
        return True, summary
