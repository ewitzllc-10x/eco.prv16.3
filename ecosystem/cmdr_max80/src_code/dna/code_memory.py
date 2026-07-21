import json, os
class CodeMemory:
    def __init__(self):
        self.file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../ram_store.json"))
        self.store = {}
        if os.path.exists(self.file):
            try: self.store = json.load(open(self.file))
            except: self.store = {}
    def _save(self):
        try: open(self.file,"w").write(json.dumps(self.store, indent=2))
        except: pass
    def remember(self, key, value):
        self.store[key]=value; self._save(); return True
    def recall(self, key):
        return self.store.get(key)
    def list(self):
        return list(self.store.keys())
