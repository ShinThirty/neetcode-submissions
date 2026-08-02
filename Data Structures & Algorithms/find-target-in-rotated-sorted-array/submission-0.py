class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search(lo, hi, p):
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if p(mid):
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        
        n = len(nums)
        m = search(0, n - 1, lambda i: nums[i] <= nums[-1])
        v = search(m, m + n - 1, lambda i: nums[i % n] >= target)
        return v % n if nums[v % n] == target else -1