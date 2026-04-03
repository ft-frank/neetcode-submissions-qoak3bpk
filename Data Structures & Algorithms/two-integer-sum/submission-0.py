class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        {}
        """
        checked = {}
        for index, number in enumerate(nums):
            search = target - number
            if search in checked:
                return [checked[search], index]
            else:
                checked[number] = index