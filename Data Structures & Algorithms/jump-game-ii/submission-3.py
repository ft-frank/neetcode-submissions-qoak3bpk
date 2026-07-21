"""
We want to find the MINIMUM number of jumps.
Intuitively I'm thinking our algorithm needs to be greedy.
At every step (deciding at index i, how far to increase i), 
we should take the answer that brings us the furtherest including the next step

For example 1:

nums = [2, 4, 1, 1, 1, 1]

At index = 0, 
you can jump to index 1 or index 2.
However index 1 has a range of index 1 + 4 or index 5
whereas jumping to index 2 has a range of 2 + 1 or index 3.
Therefore greedily take the better jump

"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0

        i = 0

        while i < len(nums) - 1:
            next_action = (0, 0) #always valid answer so 0 0 is fine
            for j in range(nums[i], 0, -1): #iteratively check each avaliable jump position
                if i + j >= len(nums) - 1:
                    return res + 1
                reach = i + j + nums[i + j]
                if reach > next_action[1]:
                    next_action = (i + j, reach)
            i = next_action[0]
            res += 1
        return res




        