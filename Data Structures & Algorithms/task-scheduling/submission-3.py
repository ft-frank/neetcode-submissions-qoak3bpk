"""
Initial Notes:

-So we must have a data structure to count all the instances of each unique task, (up to 26 unique tasks)
-Then we must sort them from largest to smallest, so that we can prioritise the task with the most 
cycles needed to be completed first.
-Then we must store them in a cycle array, where after n cycles, we put it back into the sorted array.
- We finish when there are no values within the cycle and no values within the sorted array

Data Structures:
- Count is usually using a dictionary
- Then using its dict.values, we create a max-heap, that stores the max first
- Then we grab a deque to mimic a first in first out data structure with O(1) time, like a cycle.

Algorithm:
- While loop, while values are in the heap, we continue
- Edge Case: If heap is empty, but values still in cycle, then we gotta skip to the time where
values in cycle are back in heap
"""

from collections import Counter
from heapq import heappop, heappush, heapify

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        res = 0

        count = Counter(tasks)

        max_heap = [-c for c in count.values()] #need to switch count to minus, so that in min-heap, the root is actually the highest priority

        heapify(max_heap)
        time = 0
        cycle = deque()
        while max_heap or cycle:
            time += 1
            if not max_heap:
                time = cycle[0][1]
            else:
                task = heappop(max_heap) + 1
                if task:
                    cycle.append((task, time + n)) #tuple (cycles_left, time_next_avaliable)

            
            if cycle and cycle[0][1] == time:
                heappush(max_heap, cycle.popleft()[0])
            
            
            


        return time



            
        
                


            #If len(cycle) is now > n, then remove one from cycle add it back
            #If max_heap length is now 0, then iterate through cycle to add a task back so it can continue

