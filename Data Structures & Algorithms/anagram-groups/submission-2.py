class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def to_sig(word: str):
            sig = [0] * 26
            for c in word:
                o = ord(c) - ord('a')
                sig[o] += 1
            return "#".join(str(o) for o in sig)
        
        sig_to_word = collections.defaultdict(list)
        for word in strs:
            sig = to_sig(word)
            sig_to_word[sig].append(word)
        
        return list(sig_to_word.values())