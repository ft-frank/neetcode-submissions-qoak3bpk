class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        index = 0
        output = []
        n = len(nums)
        while index < n:
            product = 1
            for j in range(n):
                if index == j:
                    continue
                else:
                    product = product * nums[j]
            output.append(product)
            index += 1
        return output   
