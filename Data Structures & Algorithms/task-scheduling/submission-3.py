class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # COUNT FREQUENCIES OF DISTINCT WORDS
        counts = Counter(tasks) #{'char' : freqs}
        maxHeap = [-c for c in counts.values()]

        # CREATE A MAXHEAP FROM FREQUENCIES
        heapq.heapify(maxHeap)

        # CREATE A DEQUE TO STORE [REMAIN_FREQ, IDLE_TIME]
        q = deque()
        time = 0

        # LOOP UNTIL NO ELEMENT IN DEQUE AND MAXHEAP
        while maxHeap or q:
            time += 1
            if maxHeap:
                # POP FROM MAXHEAP
                cnt = heapq.heappop(maxHeap) #negative
                # DECREMENT THE FREQUENCY
                cnt += 1
                # PUSH TO LAST POSITION OF QUEUE + NEXT AVAILABLE TIME
                if cnt < 0:
                    q.append([cnt, time + n])
            
            # IF IDLE TIME HAS PASSED: ADD THE CHAR BACK TO THE HEAP
            if q and time == q[0][1]:
                char = q.popleft() # [REMAIN_FREQ, IDLE_TIME]
                heapq.heappush(maxHeap, char[0]) # REMAIN_FREQ


        return time