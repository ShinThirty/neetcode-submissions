class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        n = len(s)
        seen = collections.defaultdict(int)
        res = 0
        for r, c in enumerate(s):
            if c in seen:
                l = max(l, seen[c]+1)
            seen[c] = r
            res = max(res, r - l + 1)
        
        return res
        