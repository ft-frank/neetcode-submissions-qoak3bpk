"""
During binary search, we either increase the l counter to mid + 1, or r counter to mid - 1.
How to determine which to do?

A rotated array is rotated to the right.

Therefore an array could be like:

[3, 4, 5, 6, 1, 2].
l      m        r

If mid is more than right and more than left, then the mid has increased, and therefore minimum towards right


[7, 1, 2, 3, 4, 5, 6, ]
if mid is less than left and less than right, then towards left

if mid is less than right and more than left go left


if mid is less than left and more than right: 
    not possible

When to return mid?
Return mid if the one previous to it is bigger, and the one to the right is also bigger

"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l<=r:
            m = (l + r) // 2
            left, mid, right = nums[l], nums[m], nums[r]

            res = min(res, mid)
            if mid > right:
                l = m + 1
            else:
                r = m - 1


        return res
            

