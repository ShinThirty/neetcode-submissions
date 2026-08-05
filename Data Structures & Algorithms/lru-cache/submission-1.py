class LRUCache:

    def __init__(self, capacity: int):
        self.keys = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int):
        if key not in self.keys:
            return -1

        val = self.keys.pop(key)
        self.keys[key] = val
        print(f"get {key} {self.keys}")
        return val

    def put(self, key: int, value: int):
        if key not in self.keys:
            if len(self.keys) == self.capacity:
                self.keys.popitem(last=False)
            self.keys[key] = value
        else:
            self.keys.pop(key)
            self.keys[key] = value
        print(f"put {key} {value} {self.keys}")
