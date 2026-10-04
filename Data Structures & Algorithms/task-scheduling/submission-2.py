class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxheap = [-c for c in counts.values()] #[-c values]
        heapq.heapify(maxheap) 

        q = deque() #[-c, idle]
        time = 0

        while maxheap or q:
            time += 1
            if maxheap:
                cnt = heapq.heappop(maxheap)
                cnt += 1
                if cnt != 0:
                    q.append([cnt, time + n])
            
            if q and time == q[0][1]:
                cnt = q.popleft()[0]
                heapq.heappush(maxheap, cnt)
        
        return time
            


