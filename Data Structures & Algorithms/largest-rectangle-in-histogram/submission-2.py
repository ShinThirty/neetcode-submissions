class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ms = []
        ans = -1
        for k, h in enumerate(heights + [-1]):
            while ms and heights[ms[-1]] >= h:
                j = ms.pop()
                i = -1
                if ms:
                    i = ms[-1]
                w = k - i - 1
                ans = max(ans, heights[j] * w)
            ms.append(k)
        return ans
