class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
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
                
