class CptWorkflow:
    def __init__(self):
        self.status = "BLUE"
        self.phase = "prv16.3"
    
    def execute(self, order):
        print(f"[CPT] Executing: {order}")
        return f"CPT BLUE: {order} -> 1LT + 2LT"

if __name__ == "__main__":
    wf = CptWorkflow()
    print(wf.execute("FULL CHAIN VERIFY"))
