class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_prod = res = min_prod = nums[0]

        for num in nums[1:]:

            candidates = (num, max_prod * num, min_prod * num)
            max_prod = max(candidates)
            min_prod = min(candidates)
            res = max(max_prod, res)

        return res

        