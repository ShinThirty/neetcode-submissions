class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dq = collections.deque()
        ans = []
        for r in range(n):
            while dq and nums[dq[-1]] <= nums[r]:
                dq.pop()
            dq.append(r)
            if dq[0] < r - k + 1:
                dq.popleft()
            if r >= k - 1:
                ans.append(nums[dq[0]])
        
        return ans