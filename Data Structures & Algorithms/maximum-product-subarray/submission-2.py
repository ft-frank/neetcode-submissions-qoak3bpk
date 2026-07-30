"""
Dynamic progrmaming question where we recognise that
we have to find a random lengthed subarray and the largest product.
How exactly to explain we identifed dynamic programming?
IDK


dfs(i) - where i is the index of the position of the num within nums

base_case: i >= n-1. Here we return the num at the end of the num array. 

Decision tree:

At the first number.

we have a Decision

Either multiply by next value, 
or skip to the next value completely restarting the subarray

e.g

nums = [2, 4, -3, 5]

We start at 2. 

We take the max of 2 * dfs(i + 1) or dfs(i-1)




"""



class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        #On second thought, will probably have to use a DP matrix
        #Calculating product between two indices
        n = len(nums)
        memo = [[0] * n for _ in range(n)]
        max_product = float('-inf')

        for i in range(n):
            for j in range(i, n):
                if i == j: #one num
                    memo[i][j] = nums[i]
                else: #subarray = subarray with one less char times that less char
                    memo[i][j] = memo[i][j-1] * nums[j]
                max_product = max(max_product, memo[i][j])
        return max_product

        """ 
            We use memoisation like this.

            Say we have memo[0][0] which is 2 in example 1.
            Then either:
            memo[0][1] = memo[0][1-1] * nums[1]
            or
            memo[1][1] == nums[1]

        """

        """
        Problem is that if we have a 0 that loses informatin, when we create subarray for example in an array
        like [0, 3, 4, 2]

        """

            

            
