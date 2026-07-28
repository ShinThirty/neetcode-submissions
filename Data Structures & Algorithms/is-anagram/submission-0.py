class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = collections.defaultdict(int)
        for c in s:
            chars[c] += 1
        chart = collections.defaultdict(int)
        for c in t:
            chart[c] += 1
        
        for c, n in chars.items():
            if chart[c] != n:
                return False
        for c, n in chart.items():
            if chars[c] != n:
                return False
        return True