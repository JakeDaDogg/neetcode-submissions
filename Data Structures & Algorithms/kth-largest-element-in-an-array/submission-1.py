class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = nums
        heapq.heapify(minHeap)
        kth = len(minHeap) - k
        while kth > 0:
            heapq.heappop(minHeap)
            kth-= 1

        return minHeap[0]      