class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if len(piles) == 1:
        #     return math.ceil(piles[0] / h) 
        l = 1
        r = max(piles) 
   
        while l < r :
            time = 0
            k = (l + r) // 2
            for pile in piles:
                timeTaken = math.ceil(pile/k)
                time += timeTaken
            if h >= time:
                r = k
            elif time > h:
                l = k + 1    
        return l

    