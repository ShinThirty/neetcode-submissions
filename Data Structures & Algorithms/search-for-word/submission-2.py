class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        k = len(word)
        m = len(board)
        n = len(board[0])

        found = False
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def go(x, y, i):
            nonlocal found
            if found:
                return
            
            if board[x][y] != word[i]:
                return
            
            if i == k - 1:
                found = True
                return

            c = board[x][y]
            board[x][y] = '#'
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] != '#':
                    go(nx, ny, i + 1)
            board[x][y] = c
        
        for x in range(m):
            for y in range(n):
                if not found:
                    go(x, y, 0)
        
        return found
