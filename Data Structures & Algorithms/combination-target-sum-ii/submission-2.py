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
                for j in range(freq):
                    path.append(candidate)
                    s += candidate
                    go(i + 1)
                for j in range(freq):
                    path.pop()
                    s -= candidate
        go(0)
        return res