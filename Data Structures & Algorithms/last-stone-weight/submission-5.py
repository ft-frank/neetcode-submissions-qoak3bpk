from heapq import heappush, heappop, heapify

"""
We need to implement a max-heap, to recieve the heaviest stone at all times, and insertion of
new stones. 

"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        a = [-s for s in stones] #turn negative, so we can use min-heap as a max-heap

        heapify(a) #O(n)


        while len(a) > 1:
            heaviest  = - (heappop(a))
            second_heaviest = - (heappop(a))

            if heaviest > second_heaviest:
                difference = heaviest - second_heaviest
                heappush(a, -difference)



        if a:
            return -a[0]
        return 0
