class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        used = [False]* len(nums) #bruh no way I don't know this list multipliacation.

        perm = []

        def backtrack(perm, used):
            nonlocal res
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    perm.append(nums[i])
                    used[i] = True
                    backtrack(perm, used)
                    perm.pop()
                    used[i] = False
            
        backtrack([], used)
        return res


