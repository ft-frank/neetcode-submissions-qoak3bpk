class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1 #O(n)
        if len(nums) == 1:
            return nums[0]
        while True: #remember literally the edge cases
            if l == r and l == 0:
                if nums[0] < nums[-1]:
                    return nums[0]
                else: 
                    r = len(nums) - 1
                    l = (len(nums) - 1) // 2 + 1
            mid = (l + r) // 2
            
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] < nums[mid + 1]:
                r = mid
            

