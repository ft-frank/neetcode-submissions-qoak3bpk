class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        l = 0
        r = len(nums) - 1
        while True:
            complement = target - nums[r]
            if nums[l] == complement:
                return [l + 1, r + 1]
            elif nums[l] < complement:
                l += 1
            elif nums[l] > complement:
                r -= 1


            