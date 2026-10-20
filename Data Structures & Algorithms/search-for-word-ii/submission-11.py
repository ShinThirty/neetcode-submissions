class TrieNode:
    __slots__ = ['children', 'index']
    def __init__(self):
        self.children = {}
        self.index = -1

class Trie:
    __slots__ = ['root']
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word, index):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.index = index


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1 <= board.length, board[i].length <= 12, no need to check edge cases
        m = len(board)
        n = len(board[0])

        trie = Trie()

        for index, word in enumerate(words):
            trie.add(word, index)
        
        res = []
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False] * n for _ in range(m)]

        def dfs(x, y, node):
            c = board[x][y]
            if c not in node.children:
                return

            child = node.children[c]
            visited[x][y] = True
            if child.index >= 0:
                res.append(words[child.index])
                child.index = -1
            
            for dx, dy in delta:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    dfs(nx, ny, child)
            
            visited[x][y] = False
            if len(child.children) == 0:
                del node.children[c]

        
        for x in range(m):
            for y in range(n):
                dfs(x, y, trie.root)
        
        return res
        