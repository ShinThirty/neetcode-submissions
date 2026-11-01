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
            if start == n:
                return
            go(start + 1)
            candidate, freq = freqs[start]
            j = 0
            while j < freq and s < target:
                path.append(candidate)
                s += candidate
                j += 1
                go(start + 1)
            for _ in range(j):
                s -= candidate
                path.pop()
        go(0)
        return res