class TimeMap:

    def __init__(self):
        self.data = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        
        n = len(self.data[key])
        lo = 0
        hi = n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.data[key][mid][0] > timestamp:
                hi = mid
            else:
                lo = mid + 1
        
        return self.data[key][lo - 1][1] if lo > 0 else ""
