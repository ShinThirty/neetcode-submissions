class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0
        i, j = 0, n - 1
        while i < j:
            area = min(heights[i], heights[j]) * (j - i)
            res = max(res, area)
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        
        return res