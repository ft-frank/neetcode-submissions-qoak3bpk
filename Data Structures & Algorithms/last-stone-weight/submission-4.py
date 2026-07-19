import heapq

"""
We note that we must know the two heaviest stones at each step.

This requires having a sorted data structure descending.

While loop, that ends when there is no more than one stone remaining

heap problem, best time complexity for insert and search.

"""


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        #heapify is O(n) anyways so
        stones = [-s for s in stones]
        heapq.heapify(stones) #min heap, but the values turned opposite, so the  min is actually the max
        while len(stones) > 1:
            x = -(heapq.heappop(stones)) #min turned into max
            y = -(heapq.heappop(stones)) # min turned into second max

            if y < x:
                x = x-y
                heapq.heappush(stones, -x)

        return -(stones[0]) if len(stones) > 0 else 0