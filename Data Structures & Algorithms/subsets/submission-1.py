class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        path = []
        def go(start):
            res.append(path[:])
            for i in range(start, n):
                path.append(nums[i])
                go(i + 1)
                path.pop()
        
        go(0)
        return res
