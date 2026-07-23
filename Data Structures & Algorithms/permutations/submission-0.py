"""
Permuations.

We have a recursive function.

Start at 1

We have options to append 2 or 3

Append 2

We only have 3

Append 3

How to know what options we have left?
Using a set of course





dfs(cur, left):
    for j in range(left):
        cur.append(left[j])
        left.remove


"""




class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        remaining = set(nums)
        
        def dfs(cur, left): #left as in characters left
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for j in left:
                cur.append(j) #add to current array

                dfs(cur, left - {j}) 
                cur.pop()
        dfs([], remaining)
        return res
                
