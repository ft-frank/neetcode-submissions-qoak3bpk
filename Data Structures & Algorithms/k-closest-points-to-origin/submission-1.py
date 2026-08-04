"""
K closest points mean we are potentially dealing with a heap here.

"""

from heapq import heapify, heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        distances = [(p[0]**2 + p[1]**2, p) for p in points]
        heapify(distances) #min-heap
        res = []
        for i in range(k):
            new = heappop(distances)
            res.append(new[1])

        return res

