class TimeMap:

    def __init__(self):
        self.timeLine = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeLine[key].append((timestamp, value)) # O(1)

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.timeLine[key]) - 1
        res = ""

        while l <= r:

            m = (l + r) // 2

            if self.timeLine[key][m][0] == timestamp:
                return self.timeLine[key][m][1]
            elif self.timeLine[key][m][0] > timestamp:
                r = m - 1
            else:
                res = self.timeLine[key][m][1]
                l = m + 1
        return res
        
