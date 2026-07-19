from heapq import heapify, heappop, heappush

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h, self.k = nums, k
        heapify(self.h)

        while len(self.h) > k:
            heappop(self.h) #remove the minimum


    def add(self, val: int) -> int:
        heappush(self.h, val)

        while len(self.h) > self.k:
            heappop(self.h)

        return self.h[0]        #aka the minimum
 