class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for n in s:
            if n - 1 not in s:
                con = 1
                c = n
                while c + 1 in s:
                    con += 1
                    c += 1
                res = max(res, con)
        return res
                