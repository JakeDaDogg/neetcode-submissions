from sortedcontainers import SortedDict
class TimeMap:
    def __init__(self):
        self.d = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        # Simplified: no need for .keys()
        if key not in self.d:
            return ""
        
        person = self.d[key]
        return self.binary_search(timestamp, person)
        
    def binary_search(self, target_time, sortedmap):
        search = sortedmap.keys() # Gives a view of sorted timestamps
        
        l, r = 0, len(search) - 1
        
        while l <= r:
            # Find the middle INDEX
            mid = (l + r) // 2
            # Find the middle TIMESTAMP
            mid_time = search[mid]
            
            if target_time > mid_time:
                l = mid + 1
            elif target_time < mid_time:
                r = mid - 1
            else:
                # Exact match found
                return sortedmap[mid_time]
        
        # When the loop ends, `r` points to the largest index where the time is < target_time.
        # If r < 0, it means the target_time was smaller than the very first recorded timestamp.
        if r < 0:
            return ""
            
        # Return the value tied to the timestamp at index 'r'
        return sortedmap[search[r]]


