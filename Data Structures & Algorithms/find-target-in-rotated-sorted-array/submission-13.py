class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1


        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
    

        if target > nums[-1]:
            r = l - 1
            l = 0
        else:
            r = len(nums) - 1

      
        while l <= r:
            mid_index = (l + r) // 2
            mid_value = nums[mid_index]
            if mid_value == target:
                return mid_index
            elif mid_value > target:
                r = mid_index - 1
            else:
                l = mid_index + 1
        return -1

            
            
            
