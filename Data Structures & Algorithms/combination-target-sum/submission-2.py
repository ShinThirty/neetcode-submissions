class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        path_sum = 0
        n = len(nums)

        def go(start):
            nonlocal path_sum
            if path_sum > target:
                return
            if path_sum == target:
                res.append(path[:])
                return
            
            for i in range(start, n):
                path.append(nums[i])
                path_sum += nums[i]
                go(i)
                path_sum -= nums[i]
                path.pop()
        
        go(0)
        return res
