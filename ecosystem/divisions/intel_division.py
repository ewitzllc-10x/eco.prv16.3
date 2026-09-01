from divisions.base_division import BaseDivision

class IntelDivision:
    def __init__(self, global_data):
        self.global_data = global_data

    def execute(self, packet):
        mission_id = packet["mission_id"]
        payload = packet["payload"]
        mission_type = payload.get("type", "")

        return f"[intel_division] Intel analyzing mission {mission_id} (type={mission_type})"
    def detect_patterns(self, payload):
        """Look for patterns in intel data."""
        patterns = []

        if "movement" in payload:
            mv = payload["movement"]
            if mv == "clustered":
                patterns.append("group formation detected")
            elif mv == "scattered":
                patterns.append("units dispersing")

        if "signals" in payload:
            sig = payload["signals"]
            if sig == "encrypted":
                patterns.append("encrypted comms detected")
            elif sig == "silent":
                patterns.append("signal blackout")

        return patterns

    def assess_risk(self, payload):
        """Risk scoring based on intel."""
        score = 0

        if payload.get("movement") == "clustered":
            score += 4
        if payload.get("signals") == "encrypted":
            score += 3
        if payload.get("threat_level", 0) >= 7:
            score += 5

        if score >= 10:
            return "critical"
        elif score >= 5:
            return "elevated"
        else:
            return "low"

    def generate_summary(self, intel_type, patterns, risk):
        """Produce a human-readable intel summary."""
        summary = f"Intel type: {intel_type}. Risk: {risk}. "

        if patterns:
            summary += "Patterns: " + ", ".join(patterns)
        else:
            summary += "No significant patterns detected."

        return summary

    def process(self, packet):
        payload = packet["payload"]
        mission_id = packet["mission_id"]

        self.log(f"[INTEL] Processing mission {mission_id}")

        # 1. Classify intel
        intel_type = self.classify_intel(payload)
        self.log(f"[INTEL] Type: {intel_type}")

        # 2. Detect patterns
        patterns = self.detect_patterns(payload)
        for p in patterns:
            self.log(f"[INTEL] Pattern: {p}")

        # 3. Assess risk
        risk = self.assess_risk(payload)
        self.log(f"[INTEL] Risk level: {risk}")

        # 4. Generate summary
        summary = self.generate_summary(intel_type, patterns, risk)
        self.log(f"[INTEL] Summary: {summary}")

        # 5. Recommend division or agent
        if risk == "critical":
            recommendation = "ops_division"
        elif risk == "elevated":
            recommendation = "recon_division"
        else:
            recommendation = "cmdr_max80"

        return True, f"IntelDivision completed mission | {summary} | recommended: {recommendation}"
