class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        output = []

        preFix = []
        for i in range(n):
            if i == 0:
                preFix.append(1)
            else:
                newProduct = preFix[i - 1] * nums[i - 1]
                preFix.append(newProduct)
        sufFix = []
        for i in range(n):
            if i == 0:
                sufFix.append(1)
            else:
                newProduct = sufFix[i - 1] * nums[n - i]
                sufFix.append(newProduct)
        

        for i in range(n):
            preFix[i] = preFix[i] * sufFix[n - 1 - i]
        
        return preFix




