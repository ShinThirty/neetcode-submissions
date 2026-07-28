class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l, r = 0, 0
        n = len(s)
        seen = set()
        while r < n:
            nxt = s[r]
            while nxt in seen:
                seen.remove(s[l])
                l += 1
            seen.add(nxt)
            r += 1
            res = max(res, r - l)
        
        return res