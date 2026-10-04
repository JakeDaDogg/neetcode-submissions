class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = numbers
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] + s[j] > target:
                j -= 1
            if s[i] + s[j] < target:
                i += 1
            if s[i] + s[j] == target:
                return [i+1, j+1]