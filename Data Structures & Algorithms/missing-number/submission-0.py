class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums) #this will be cancelled out with the final number
        for i in range(len(nums)): #len(nums) doesn't have to indicate that is 0->n
            res = res ^ i
            res = res ^ nums[i]
        
        return res