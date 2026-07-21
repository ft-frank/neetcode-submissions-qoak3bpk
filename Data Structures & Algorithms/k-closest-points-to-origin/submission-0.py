"""
Initial Notes:

- We have to develop a sorted array that stores the difference between a point and the origin. 
- This array is sorted by the distance, in non-decreasing order,
as this will allow us to return the 1st closest integer if k = 1, and so on.
- What I am thinking here is a heap data structure.
This is because we will have to be iterating through the 2-D array points,
where we calculate the distance to the origin, and then insert it into our data structure.
A heap has the best insert time complexity of O(log n) when an array has to be sorted,
because a heap attempts to insert the score in the right position at insert, instead
of needing to be sorted later.

Plan:

We iterate through points
Create a tuple of the (distance, point)
Insert tuple into heap


OR.

Create a defaultdict, where each distance stores a list of points with that distance
Then we store the distances in a min-heap
Use each popped value to grab a value from the default dict. 


"""
from collections import defaultdict
from heapq import heappop, heappush, heapify



class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dic = defaultdict(list)
        res = []
        min_heap = []
        for p in points:
            x = p[0]
            y = p[1]

            distance = x**2 + y**2

            dic[distance].append(p)
            min_heap.append(distance)

        heapify(min_heap)

        for i in range(k):
            dis = heappop(min_heap)
            res.append(dic[dis].pop())

        return res
        