class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        freqs = list(Counter(nums).items())
        n = len(freqs)
        res = []
        path = []

        def go(start):
            res.append(path[:])

            for i in range(start, n):
                num, freq = freqs[i]
                for j in range(freq):
                    path.append(num)
                    go(i + 1)
                for _ in range(freq):
                    path.pop()
        
        go(0)
        return res