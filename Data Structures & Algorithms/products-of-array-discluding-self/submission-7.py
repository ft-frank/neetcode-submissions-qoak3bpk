class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        l = 1
        for i in range(len(nums)):
            prefix.append(l)
            l = l * nums[i]
        
        suffix = []
        r = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix.append(r)
            r = r * nums[i]

        res = [prefix[i] * suffix[-i - 1] for i in range(len(nums))]
        return res



        