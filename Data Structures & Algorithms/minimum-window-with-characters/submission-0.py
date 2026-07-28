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

        def adjust_matches(before, after):
            nonlocal matches
            if not before and after:
                matches += 1
            if before and not after:
                matches -= 1

        while r < len(s) or matches == target:
            if matches == target:
                new_size = r - l
                if new_size < res_size:
                    res_size = new_size
                    resl, resr = l, r
                if s[l] in tc:
                    before = sc[s[l]] >= tc[s[l]]
                    sc[s[l]] -= 1
                    if sc[s[l]] == 0:
                        del sc[s[l]]
                    after = sc[s[l]] >= tc[s[l]]
                    adjust_matches(before, after)
                l += 1
            elif r < len(s):
                if s[r] in tc:
                    before = sc[s[r]] >= tc[s[r]]
                    sc[s[r]] += 1
                    after = sc[s[r]] >= tc[s[r]]
                    adjust_matches(before, after)
                r += 1
            

        return s[resl:resr]
