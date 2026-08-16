""
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) #O(n)
        res = float('inf')
        while l <= r: #be careful of off by one errors.
            mid = (l + r) // 2
            k = 0
            for p in piles:
                k += math.ceil(p / mid) #wrong logic here. 

            if k <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

            #Only save answers that can complete piles within h hours. k records how many hours we use.
            



        return res
        