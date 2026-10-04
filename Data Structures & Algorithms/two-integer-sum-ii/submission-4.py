class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        m = numbers[l] + numbers[r]
        while m != target:
            if m > target:
                r -= 1
            if m < target:
                l += 1
            m = numbers[l] + numbers[r]
        return [l+1, r+1]
