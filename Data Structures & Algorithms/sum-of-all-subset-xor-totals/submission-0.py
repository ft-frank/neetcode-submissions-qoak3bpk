class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        res = 0
        xor = 0
        n = len(nums)

        def backtrack(i):
            nonlocal xor
            if i >= n: #base_case, stop here
                nonlocal res
                res += xor
                return
            
            prev = xor #save this, so that I can backtrack

            #First, include the current num in the subset, then move onto next
            if xor == 0:
                xor = nums[i]
            else:
                xor = xor ^ nums[i]
            backtrack(i + 1)

            #backtracking step

            xor = prev

            # go to next number without including current one

            backtrack(i + 1)

            



        backtrack(0)
        return res