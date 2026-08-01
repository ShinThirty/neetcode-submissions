class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def search(lo, hi, p):
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if p(mid):
                    hi = mid
                else:
                    lo = mid + 1
            
            return lo
        
        def predicate(k):
            return sum([(p + k - 1) // k for p in piles]) <= h

        return search(1, max(piles), predicate)