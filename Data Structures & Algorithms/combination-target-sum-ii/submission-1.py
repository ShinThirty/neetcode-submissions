class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        s = 0
        freqs = list(Counter(candidates).items())
        n = len(freqs)

        def go(start):
            nonlocal s
            if s > target:
                return
            if s == target:
                res.append(path[:])
                return

            for i in range(start, n):
                candidate, freq = freqs[i]
                for j in range(1, freq + 1):
                    for _ in range(j):
                        path.append(candidate)
                        s += candidate
                    go(i + 1)
                    for _ in range(j):
                        s -= candidate
                        path.pop()
        go(0)
        return res