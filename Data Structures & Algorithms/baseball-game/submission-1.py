"""
We use a simple LIFO stack.

We iterate through the array ops,

following the rules of the record.
We then return the sum of all the scores within our stack.

The time complexity of iterating through the array ops, and performing actions. 
Each action is an O(1) action, and we do O(n) operations, therefore
the total is O(n)

The final summation at the end can be simply another run through our stack, which worse-case is O(n), 
or we can keep a running count.

The final complexity will be the same so yeah.


"""

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []
        for o in operations:
            if o == "+":
                stack.append(stack[-1] + stack[-2]) #grabs from stack
            elif o == "D":
                stack.append(stack[-1] * 2) #grabs from stack
            elif o == "C":
                stack.pop() #removes from stack
            else:
                stack.append(int(o))

        return sum(stack)