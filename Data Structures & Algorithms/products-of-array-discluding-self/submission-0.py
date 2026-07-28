class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 0 -> [0, 0)
        # i -> [0, i)
        prefix = [1]
        for num in nums:
            prefix.append(prefix[-1] * num)
        suffix = [1] # suffix[i] = multiply [i + 1, n)

        # 0 -> [n, n)
        # 1 -> [n - 1, n)
        # j -> [n - j, n)
        # n - j = i + 1
        # j = n - i - 1

        # answer[i] = prefix[i] * suffix[n - i - 1]

        for i in range(n - 1, -1, -1):
            suffix.append(suffix[-1] * nums[i])
        
        res = [1] * n
        for i in range(n):
            res[i] = prefix[i] * suffix[n - i - 1]
        
        return res
