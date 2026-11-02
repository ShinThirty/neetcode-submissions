class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def go():
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i, num in enumerate(nums):
                if num != -11:
                    nums[i] = -11
                    path.append(num)
                    go()
                    path.pop()
                    nums[i] = num
        
        go()

        return res