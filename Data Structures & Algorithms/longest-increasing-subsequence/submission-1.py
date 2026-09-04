"""
Integer array nums.

Valid: 1, 2, 3, 4, 5, 6, 7, 8, 9


"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        memo = {}
        n = len(nums)

        def dfs(i):
            if i in memo: #if this index has already been calculated, return it
                return memo[i]
            if i >= n-1: #if index is the last_character or after, include the current character by running 1 (a subsequence started at this last index has a length of 1)
                return 1
            res = 1
            for j in range(i, n): #for every index from this index to the end
                if nums[j] > nums[i]: #check if the later index is larger than the earlier index
                    #res the max between res (subsequence ends here) or 1 (include this character) + dfs(j) search
                    #for longest subsequence later than index
                    res = max(res, 1 + dfs(j)) #the best subsequence including that point either ends there, or includes the next one. Decide which using max.
            memo[i] = res #finally the memo will return 

            return memo[i]
        return max(dfs(i) for i in range(n))
            