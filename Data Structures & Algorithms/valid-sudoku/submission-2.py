class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == '.':
                    continue
                box = (r // 3, c // 3)
                
                if v in rows[r] or v in cols[c] or v in boxes[box]:
                    return False

                rows[r].add(v)
                cols[c].add(v)
                boxes[box].add(v)
        
        return True