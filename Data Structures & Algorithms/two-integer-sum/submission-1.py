class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index in range(len(nums)):
            search = target - nums[index]
            if search in seen:
                return [seen[search], index]
            else:
                seen[nums[index]] = index


 