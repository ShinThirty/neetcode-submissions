class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            l = str(len(s))
            l = '0' * (3 - len(l)) + l
            res.append(l)
            res.append(s)
        
        return "".join(res)
            

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            l = int(s[i:i+3])
            j = i + 3
            word = s[j:j+l]
            res.append(word)
            i = j + l
        
        return res
