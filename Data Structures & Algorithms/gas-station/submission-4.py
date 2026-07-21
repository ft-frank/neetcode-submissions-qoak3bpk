"""
Initial Notes:

- We have to detect a cycle within the 'linked list'. 

A brute force naive approach, is to iterate through gas to
test each starting point, and then attempt to complete the circuit,
where our first completion of the circuit, we just return the answer
as there is only one Solution

We can implement a greedy solution knowing that this is a cycled list.


We first must keep track of how much gas we have each step, taking 
into account how much gas to get to next station.

This is gas[i] - cost[i]

We iterate through the array and keep track of the total of
this value, 


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
        



