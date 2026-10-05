class MedianFinder:

    def __init__(self):
        self.s, self.l = [], []
        heapq.heapify(self.s)
        heapq.heapify(self.l)

    def addNum(self, num: int) -> None:
        # add to maxheap (s)
        heapq.heappush(self.s, -num)

        # if min of s > max of l: swap elements
        if self.l and -self.s[0] > self.l[0]:
            max_s = heapq.heappop(self.s)
            min_l = heapq.heappop(self.l)
            heapq.heappush(self.l, -max_s)
            heapq.heappush(self.s, -min_l)
        # if size of s > size of l + 1 or vise versa: push element to lesser size heap
        if len(self.s) == len(self.l) + 1:
            max_s = heapq.heappop(self.s)
            heapq.heappush(self.l, -max_s)
        
        elif len(self.l) == len(self.s) + 1:
            min_l = heapq.heappop(self.l)
            heapq.heappush(self.s, -min_l)

        
    def findMedian(self) -> float:
        if len(self.l) == len(self.s):
            return (self.l[0] - self.s[0])/2
        
        elif len(self.l) > len(self.s):
            return self.l[0]
        
        else:
            return -self.s[0]

        
        