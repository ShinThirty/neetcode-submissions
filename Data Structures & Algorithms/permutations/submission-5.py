class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def go(start):
            if start == n - 1:
                res.append(nums[:])
            
            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                go(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        
        go(0)
        return res