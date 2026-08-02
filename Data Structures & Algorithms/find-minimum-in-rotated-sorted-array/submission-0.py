class Solution:
    def findMin(self, nums: List[int]) -> int:
        def search(lo, hi, p):
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if p(mid):
                    hi = mid
                else:
                    lo = mid + 1
            
            return lo
        
        return nums[search(0, len(nums) - 1, lambda i: nums[i] <= nums[-1])]