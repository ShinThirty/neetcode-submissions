class TrieNode:
    # __slots__ = ('children', 'end')
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
        if idx == len(word):
            return root.end
        else:
            i = idx
            while i < len(word) and word[i] != '.':
                if word[i] not in cur.children:
                    return False
                cur = cur.children[word[i]]
                i += 1
            if i == len(word):
                return cur.end
            else:
                for c in cur.children:
                    child = cur.children[c]
                    if self._search_internal(child, word, i + 1):
                        return True
                return False

    def search(self, word: str) -> bool:
        return self._search_internal(self.root, word, 0)
