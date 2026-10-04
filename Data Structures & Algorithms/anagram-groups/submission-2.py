class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for s in strs:
            w = ''.join(sorted(s))
            if w in dic.keys():
                dic[w].append(s)
            else:
                dic[w] = [s]

        return list(dic.values())