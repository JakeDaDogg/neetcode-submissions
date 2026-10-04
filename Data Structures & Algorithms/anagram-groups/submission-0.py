class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sword = ''.join(sorted(s))
            res[sword].append(s)
        
        return list(res.values())
        