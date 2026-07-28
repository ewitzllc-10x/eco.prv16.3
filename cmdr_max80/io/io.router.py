class CmdrIoRouter:
    def route(self, cmd):
        print(f"[CMDR MAX80 IO] Right hand routing for Admiral: {cmd}")
        return f"CMDR ROUTED: {cmd}"
