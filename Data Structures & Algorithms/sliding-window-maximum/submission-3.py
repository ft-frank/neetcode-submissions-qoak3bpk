"""
Pattern: We have to find the maximum element within a a set amount of elements. Therefore a max-heap could be useful.




"""

from heapq import heapify, heappush, heappop


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    
        cur = [(-nums[n], n) for n in range(k)] #creates max-heap using negative. Because heapify creates min-heap. Include index, so that we can exclude if not good.

        heapify(cur)

        res = []

        for j in range(k, len(nums) + 1): #adds the rest of the elements until end
            #grabbing maximum logic for that current heap
            min_index = j - k
            while cur[0][1] < min_index: #while the maximum is not within the last k elements
                heappop(cur) #get rid of it, its irrelevant
            maximum = cur[0][0] #now grab he maximum, and thenturn it back into its actual value
            res.append(-maximum) #reverts back to the original value

            #adding the next value
            if j < len(nums):
                new = (-nums[j], j)
                heappush(cur, new)
        #off by one case, missing last value
        return res






        

        
             