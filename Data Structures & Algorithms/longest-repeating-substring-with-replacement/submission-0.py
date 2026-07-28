class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = Counter()
        maxf = 0
        n = len(s)
        l = 0
        for r in range(n):
            freq[s[r]] += 1
            maxf = max(maxf, freq[s[r]])
            if r - l + 1 - maxf > k:
                freq[s[l]] -= 1
                l += 1
        
        return r - l + 1