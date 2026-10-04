# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs)-1)
        return pairs
    
    def quickSortHelper(self, pairs:List[Pair], s: int, e: int) -> List[Pair]:
        length = e - s + 1
        if length <= 1:
            return
        pivot = pairs[e]
        lp = s
        for i in range(s, e):
            if pairs[i].key < pivot.key:
                pairs[lp], pairs[i] = pairs[i], pairs[lp]
                lp += 1

        pairs[lp], pairs[e] = pairs[e], pairs[lp]

        self.quickSortHelper(pairs, s, lp-1)
        self.quickSortHelper(pairs, lp+1, e)
        return pairs