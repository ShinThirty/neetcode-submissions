from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tc = Counter()
        for t_c in t:
            tc[t_c] += 1
        target = len(tc)
        sc = Counter()
        matches = 0
        l, r = 0, 0
        res_size, resl, resr = float('inf'), 0, 0

        while r < len(s) or matches == target:
            if matches == target:
                new_size = r - l
                if new_size < res_size:
                    res_size = new_size
                    resl, resr = l, r
                if s[l] in tc:
                    if sc[s[l]] == tc[s[l]]:
                        matches -= 1
                    sc[s[l]] -= 1
                    if sc[s[l]] == 0:
                        del sc[s[l]]
                l += 1
            else:
                if s[r] in tc:
                    sc[s[r]] += 1
                    if sc[s[r]] == tc[s[r]]:
                        matches += 1
                r += 1

        return s[resl:resr]
