class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = len(nums)
        buckets = [[] for _ in range(m + 1)]
        
        freq = Counter(nums)
        for n, f in freq.items():
            buckets[f].append(n)
        
        res = []
        for i in range(m, -1, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res