class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            looking = target - num
            if looking in seen:
                return [seen[looking], i]
            else:
                seen[num] = i
                