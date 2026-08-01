class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        
        def search(lo, hi, p):
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if not p(mid):
                    lo = mid + 1
                else:
                    hi = mid
            
            return lo
        
        row = search(0, m - 1, lambda r: matrix[r][-1] >= target)
        col = search(0, n - 1, lambda c: matrix[row][c] >= target)

        return matrix[row][col] == target