class TrieNode:
    __slots__ = ['children', 'end']
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    __slots__ = ['root']
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1 <= board.length, board[i].length <= 12, no need to check edge cases
        m = len(board)
        n = len(board[0])

        trie = Trie()

        for word in words:
            trie.add(word)
        
        res = []
        working_path = []
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False] * n for _ in range(m)]

        def dfs(x, y, node):
            nonlocal res, working_path
            c = board[x][y]
            if c not in node.children:
                return

            node = node.children[c]
            working_path.append(c)
            visited[x][y] = True
            if node.end:
                res.append("".join(working_path))
                node.end = False
            
            for dx, dy in delta:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    dfs(nx, ny, node)
            
            working_path.pop()
            visited[x][y] = False

        
        for x in range(m):
            for y in range(n):
                dfs(x, y, trie.root)
        
        return res
        