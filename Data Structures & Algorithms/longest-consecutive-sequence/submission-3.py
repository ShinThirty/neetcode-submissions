class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for n in s:
            if n - 1 not in s:
                c = n
                while c + 1 in s:
                    c += 1
                res = max(res, c - n + 1)
        return res
                