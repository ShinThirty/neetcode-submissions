class TrieNode:
    __slots__ = ('children', 'end')
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True
    
    def _search_internal(self, root: TrieNode, word: str, idx: int) -> bool:
        cur = root
        i = idx
        while i < len(word) and word[i] != '.':
            cur = cur.children.get(word[i])
            if cur is None:
                return False
            i += 1
        if i == len(word):
            return cur.end
        else:
            return any(self._search_internal(child, word, i + 1) for child in cur.children.values())

    def search(self, word: str) -> bool:
        return self._search_internal(self.root, word, 0)
