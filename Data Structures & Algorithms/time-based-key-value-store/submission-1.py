from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.structure = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.structure[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.structure[key]) - 1
        #binary search for the minimum
        saved = ""
        saved_timestamp = 0
        while l <= r:
            mid = (l + r) // 2
            mid_time = self.structure[key][mid][0]
            if mid_time == timestamp:
                return self.structure[key][mid][1]
            elif mid_time < timestamp:
                if mid_time > saved_timestamp:
                    saved = self.structure[key][mid][1]
                    saved_timestamp = mid_time
                l = mid + 1
            else:
                r = mid - 1
            

        return saved
                

        
