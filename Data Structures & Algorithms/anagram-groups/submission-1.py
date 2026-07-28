class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def to_sig(word: str):
            sig = [0] * 26
            for c in word:
                o = ord(c) - ord('a')
                sig[o] += 1
            return "#".join(str(o) for o in sig)
        
        sig_to_word = {}
        for word in strs:
            sig = to_sig(word)
            if sig not in sig_to_word:
                sig_to_word[sig] = []
            sig_to_word[sig].append(word)
        
        res = []
        for s in sig_to_word.values():
            res.append(s)

        return res