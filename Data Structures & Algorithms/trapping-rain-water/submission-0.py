class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax, rightMax = 0, 0
        n = len(height)
        l, r = 0, n - 1
        res = 0
        while l < r:
            leftMax = max(leftMax, height[l])
            rightMax = max(rightMax, height[r])
            if leftMax <= rightMax:
                res += leftMax - height[l]
                l += 1
            else:
                res += rightMax - height[r]
                r -= 1
        
        return res