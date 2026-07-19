from heapq import heapify, heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int: 

        heapify(nums) #min-heap, now keeps the minimum to the largest

        while len(nums) > k:
            heappop(nums) #remove the min, until there are k elements left

        return nums[0]

