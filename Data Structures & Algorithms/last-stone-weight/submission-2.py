#using heaviest and lightest only means its a heap/priority queue question

from heapq import heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        heap = []

        for weight in stones:
            heappush(heap, 0 - weight)
        
        
        while len(heap) > 1:
            stone1 = heappop(heap)
            stone2 = heappop(heap)
            if stone1 == stone2:
                continue
            else:
                if stone1 < stone2:
                    newStone = stone1 - stone2
                elif stone2 > stone1:
                    newStone = stone2 - stone1
                heappush(heap, newStone)

        return 0 - heap[0] if len(heap) >= 1 else 0
        
