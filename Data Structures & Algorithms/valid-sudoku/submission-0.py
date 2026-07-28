class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def next_grid(x: int, y: int) -> (int, int):
            ny = y + 1
            if ny % 3 == 0:
                return x + 1, ny - 3
            else:
                return x, ny
        
        for x in range(9):
            seen = set()
            for y in range(9):
                if board[x][y] in seen:
                    print(board[x][y])
                    return False
                if board[x][y] != '.':
                    seen.add(board[x][y])
        
        for y in range(9):
            seen = set()
            for x in range(9):
                if board[x][y] in seen:
                    return False
                if board[x][y] != '.':
                    seen.add(board[x][y])

        x, y = 0, 0
        for _ in range(9):
            seen = set()
            for _ in range(9):
                if board[x][y] in seen:
                    return False
                if board[x][y] != '.':
                    seen.add(board[x][y])
                x, y = next_grid(x, y)
            if x == 9:
                x = 0
                y += 3
        
        return True
            