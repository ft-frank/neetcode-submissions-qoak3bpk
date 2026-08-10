"""
Return N choose K.

We have a recursive function backtrack.
It takes in a number as its argument, 1 is the base case.
Using that index, it chooses to include that integer, and runs backtrack on the next integer.
Once it returns, we exclude that integer.

Once a response is k long, we add it to res, and then return.

We stop calling the recursion once the integer is more than n.

"""



class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        current = []

        def backtrack(i):
            if len(current) == k:
                res.append(current.copy())
                return 
            elif i > n:
                return 
            current.append(i)
            backtrack(i + 1)
            current.pop()
            backtrack(i + 1)   


        backtrack(1)
        return res      