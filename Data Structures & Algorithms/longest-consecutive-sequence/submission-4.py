class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for x in s:
            if x - 1 not in s:
                end = x
                while end + 1 in s:
                    end += 1
                res = max(res, end - x + 1)
        return res