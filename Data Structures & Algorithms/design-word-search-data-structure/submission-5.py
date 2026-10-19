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
    
    def _search_internal(self, word: str, node: TrieNode, i: int) -> bool:
        while i < len(word) and word[i] != '.':
            node = node.children.get(word[i])
            if node is None:
                return False
            i += 1
        if i == len(word):
            return node.end
        else:
            return any(self._search_internal(word, child, i + 1) for child in node.children.values())

    def search(self, word: str) -> bool:
        return self._search_internal(word, self.root, 0)
