class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) # O(n) operation
        res = float("infinity")
        k = float("infinity")

        while l <= r:
            mid = (l + r) // 2 
            hours = 0

            for pile in piles:
                pile_time = math.ceil(pile/mid)
                hours += pile_time

            if hours <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
    
        
        return res