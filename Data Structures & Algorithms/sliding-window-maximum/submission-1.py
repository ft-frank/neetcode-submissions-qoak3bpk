from collections import deque

"""
For example 1:

first window = [1, 2, 1], where the maximum is 2

res = [2]


Brute force solution would be to use the max() function on every sliding window using a subarry from l->r pointer, where r - l + 1 would be k.
Time complexity of this solution would be O(k*n).

An ideal solution should theortically be O(n), as we attempt to keep track of the maximum as we look through each sliding window within the array.

[1, 2]

Maybe switch heads everytime max is switched?




"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        """Brute Force"""


        res = []
        l = 0
        r = k

        while r <= len(nums):
            subarray = nums[l:r]
            maximum = max(subarray)
            res.append(maximum)
            l += 1
            r += 1

        return res

    