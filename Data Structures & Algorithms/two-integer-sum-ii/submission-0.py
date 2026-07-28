class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i < j:
            s = numbers[i] + numbers[j]
            if s < target:
                i += 1
                continue
            if s > target:
                j -= 1
                continue
            break
        return [i + 1, j + 1]