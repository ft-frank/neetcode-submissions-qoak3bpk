class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        indexes = []
        for i in range(len(nums)):
            if nums[i] == val:
                indexes.append(i)
        i = 0
        for index in indexes:
            nums.pop(index - i)
            i += 1        
        return len(nums)