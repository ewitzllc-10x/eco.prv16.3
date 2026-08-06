class CptMemory:
    def __init__(self):
        self.store = {}
    def save(self, k, v):
        self.store[k] = v
    def recall(self, k):
        return self.store.get(k)
