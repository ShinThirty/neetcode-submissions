class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        part = {}
        for i, n in enumerate(nums):
            if n in part:
                return [part[n], i]
            else:
                part[target - n] = i