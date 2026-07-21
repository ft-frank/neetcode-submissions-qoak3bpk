"""
Initial Notes:

- We have to detect a cycle within the 'linked list'. 

A brute force naive approach, is to iterate through gas to
test each starting point, and then attempt to complete the circuit,
where our first completion of the circuit, we just return the answer
as there is only one Solution

However, what we can do is greedily start at indexes that are possible to get to next round 
in the first place

For example 1:

[- 1, 0, -1, 3]. Then take the highest gas value if summation > 0


For example 2:

[-1, -1, 1]. Summation < 0, therefore not enough gas.

Example 7:

[-1, 3, -4, 2]

"""



class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        summation = [gas[i] - cost[i] for i in range(n)]
        if sum(summation) < 0:
            return -1
        #now only iterate through the positive values

        total = 0
        res = 0
        for j in range(n):
            total += summation[j]
            if total < 0:
                total = 0
                res = j + 1
        return res
        



