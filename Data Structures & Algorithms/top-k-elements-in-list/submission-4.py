class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int) # (key, val) = (n (int), freq (int))
        for n in nums:
            if n in d.keys():
                d[n] += 1
            else:
                d[n] = 0
        
        return sorted(d, key=d.get, reverse=True)[:k]
