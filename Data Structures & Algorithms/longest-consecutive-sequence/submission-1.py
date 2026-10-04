class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # sort nums from low to high
        sortedN = sorted(nums)
        # sol is the solution, seqeunce is the current longest sequence
        sol = 1
        sequence = [sortedN[0]]
        
        # iterate through the array to find 
        for i in range(1, len(nums)):
            if sequence[-1] + 1 == sortedN[i]:
                sequence.append(sortedN[i])
                length = len(sequence)
                if length >= sol: 
                    sol = length
            
            if sequence[-1] == sortedN[i]:
                continue

            else: 
                sequence = [sortedN[i]]
                length = 1
            
            
        
        return sol
        