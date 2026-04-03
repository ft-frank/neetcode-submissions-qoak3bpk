class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            
            # If mid element is greater than rightmost element,
            # minimum must be in the right half
            if nums[mid] > nums[r]:
                l = mid + 1
            # Otherwise, minimum is in the left half (including mid)
            else:
                r = mid
        
        # When l == r, we've found the minimum
        return nums[l]