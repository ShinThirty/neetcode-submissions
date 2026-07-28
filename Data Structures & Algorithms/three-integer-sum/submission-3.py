class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)
        n = len(snums)
        i = 0
        res = []
        while i < n - 2:
            if i > 0 and snums[i] == snums[i - 1]:
                i += 1
                continue
            a = snums[i]
            if a > 0:
                break
            j = i + 1
            k = n - 1
            while j < k:
                if j > i + 1 and snums[j] == snums[j - 1]:
                    j += 1
                    continue
                if k < n - 1 and snums[k] == snums[k + 1]:
                    k -= 1
                    continue
                s = snums[j] + snums[k]
                if s < -a:
                    j += 1
                elif s > -a:
                    k -= 1
                else:
                    res.append([a, snums[j], snums[k]])
                    j += 1
                    k -= 1
            i += 1
        
        return res