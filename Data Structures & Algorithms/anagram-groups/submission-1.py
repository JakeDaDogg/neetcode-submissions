class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 1:
            return [strs]
        
        sol = defaultdict(list)
        for string in strs:
            sorteds = ''.join(sorted(string))
            sol[sorteds].append(string)
        
        return list(sol.values())

            
        