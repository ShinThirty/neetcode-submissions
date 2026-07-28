class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = collections.defaultdict(int)
        for c in s:
            chars[c] += 1
        chart = collections.defaultdict(int)
        for c in t:
            chart[c] += 1
        
        return chars == chart