class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        path = []

        def go(start):
            if start == n:
                res.append(path[:])
                return
            
            for end in range(start + 1, n + 1):
                i, j = start, end - 1
                while i < j and s[i] == s[j]:
                    i += 1
                    j -= 1
                if i >= j:
                    path.append(s[start:end])
                    go(end)
                    path.pop()
        
        go(0)
        return res
                