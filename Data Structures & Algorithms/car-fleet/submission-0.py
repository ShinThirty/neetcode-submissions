class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        order = sorted(range(n), key=lambda i: -position[i])
        t_i = -float('inf')
        res = 0
        for j in order:
            t_j = (target - position[j]) / speed[j]
            if t_i < t_j:
                res += 1
                t_i = t_j
        return res
