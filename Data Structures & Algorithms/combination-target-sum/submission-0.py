"""
Backtracking.



Decistion tree.

To increase the count by 1 of this particular number, or skip it.
We break the recursion when the sum is over the target.

E.g

Iterating over the array nums


We choose to add a 2, or not add a 2.

2. We choose to add a 2, or not add a 2 and go to the next num.

4. Again

6. Again

8. Again

10. Over the target, we don't want to add a 2. Remove the 2 and move on 

Time complexity:

Space complexity: 

"""




class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []


        def dfs(i):
            if i >= len(nums):
                return
            if sum(subset) > target:
                return #not a valid answer, we don't want to continue down this path
            elif sum(subset) == target:
                res.append(subset.copy()) #valid answer, however adding anymore to this subset is not good, therefore we return
                return
            subset.append(nums[i]) #we choose to add a num[i]
            dfs(i)  #we choose to add another num[i]
            subset.pop() #we remove that extra num[i]
            dfs(i+1) #we move onto the next num[i]

            
        dfs(0)
        return res