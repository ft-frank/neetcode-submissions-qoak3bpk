""" 
Find the largest indicates that this problem could possibly be solved using
a greedy algorithm

We iterate through the array, and at every step, determine if
1. the next value increases value of subArray 
2. a while loop of the left value, checking to see if removing it increases value
3. Save result
4. I need a base case as well
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, 0
        current_val = res
        while r < len(nums) - 1:
            if current_val + nums[r+1] > nums[r+1]:
                r += 1
            else:
                r += 1 
                l = r
            current_val = sum(nums[l:r+1])
            res = max(res, current_val)
        return res