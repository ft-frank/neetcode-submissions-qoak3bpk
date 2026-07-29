"""
We use a top-down dynamic programming approach with memoisation. 

We create a hashMap, that records the maximum money that you can earn if you rob starting from that house to the end of the street.
These are our subproblems, where each subproblem is to solve the maximum amount of money you can rob without alterting the police within 
the current house and the houses to the right of it on the street.

Within our decision tree, we have two options at each house.

Either, skip the current house and rob the next house, or rob the current house and rob the next house 2 streets over. 



"""



class Solution:
    def rob(self, nums: List[int]) -> int:

        hashMap = {}
        
        def dfs(i):
            if i >= len(nums): #base_case, we rob no houses
                return 0
            if i in hashMap:
                return hashMap[i]#we retrieive cached result from previous recursive call
            hashMap[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return hashMap[i]
            
        return dfs(0)
                
            
            
