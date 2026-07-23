"""
Optimal backtracking solution.

1. Pruning - eliminating redundant runs
2. Sorting - allows our algorithm to identify redundant runs
"""


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            

            for j in range(i, len(nums)): #for every number after the current number in the sorted array
                if total + nums[j] > target:
                    return #stops the function when we know that all numbers from now on added to the array will not be a good answer
                
                cur.append(nums[j])
                dfs(j, cur, total + nums[j]) #only run the recursive function when knowing it could lead to a right answer (pruning was before)

                cur.pop()

        dfs(0, [], 0)
        return res
                

