class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = float('inf')
        res = 0
        for p in prices:
            res = max(res, max(0, p - b))
            b = min(b, p)
        return res
