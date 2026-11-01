class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        s = 0
        freqs = list(Counter(candidates).items())
        n = len(freqs)

        def go(start):
            nonlocal s
            if s == target:
                res.append(path[:])
                return
            
            for i in range(start, n):
                candidate, freq = freqs[i]
                j = 0
                while j < freq and s + candidate <= target:
                    j += 1
                    path.append(candidate)
                    s += candidate
                    go(i + 1)
                
                s -= candidate * j
                for _ in range(j):
                    path.pop()
        go(0)
        return res