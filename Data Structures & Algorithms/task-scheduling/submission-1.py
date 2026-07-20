from heapq import heapify, heappop, heappush
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        heapify(maxHeap) #max-heap of counts. 

        #Here, I don't want any of the values within the heap crossing 0, we can check on the cycle
        cycle = deque()
        time = 0
        
        while maxHeap or cycle:
            time += 1

            if not maxHeap:
                time = cycle[0][1]
            
            else:
                cnt = 1 + heappop(maxHeap)
                if cnt:
                    cycle.append([cnt, time + n])
            if cycle and cycle[0][1] == time:
                heappush(maxHeap, cycle.popleft()[0])
        return time


