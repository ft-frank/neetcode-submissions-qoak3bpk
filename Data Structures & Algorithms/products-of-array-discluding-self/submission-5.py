class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        output = [1] * n
        output[0] = 1
        for i in range(1, n, 1):
            output[i] = output[i - 1] * nums[i - 1]

        suf = [1] * n
        suf[0] = 1
        for i in range(1, n, 1):
            suf[i] = suf[i - 1] * nums[n - i]

        for i in range(n):
            output[i] = output[i] * suf[n - 1 - i]
        return output

    
        





