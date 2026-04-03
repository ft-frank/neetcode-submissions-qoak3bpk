class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefixProduct = [1] * n
        prefixProduct[0] = 1
        for i in range(1, n, 1):
            prefixProduct[i] = prefixProduct[i - 1] * nums[i - 1]

        suffixProduct = [1] * n
        suffixProduct[0] = 1
        for i in range(1, n, 1):
            suffixProduct[i] = suffixProduct[i - 1] * nums[n - i]
        output = []
        for i in range(n):
            output.append(prefixProduct[i] * suffixProduct[n - 1 - i])
        return output
        





