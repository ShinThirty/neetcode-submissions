class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if m < n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        # m >= n
        k = (m + n) // 2
        lo = (m - n) // 2
        hi = (m + n) // 2
        while lo < hi:
            i = lo + (hi - lo) // 2
            j = k - i
            if nums1[i] >= nums2[j - 1]:
                hi = i
            else:
                lo = i + 1
        
        i = lo
        j = k - i
        ans = float('inf')
        if i < m:
            ans = nums1[i]
        if j < n:
            ans = min(ans, nums2[j])
        if (m + n) % 2 == 0:
            ans2 = -float('inf')
            if j > 0:
                ans2 = nums2[j - 1]
            if i > 0:
                ans2 = max(nums1[i - 1], ans2)
            ans = (ans + ans2) / 2

        return ans