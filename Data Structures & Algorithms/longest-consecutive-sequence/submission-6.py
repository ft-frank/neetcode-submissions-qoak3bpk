

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums) #duplicates don't matter.

        longest = 0 #have to keep track of output
        length = 1
        for num in nums: #O(n)
            #how to start a sequence, either a number is num + 1 or num - 1.
            if num - 1 not in nums: #O(1) lookup
                length = 1
                while num + length in nums: #sequence continues if num + 1 in sequence
                    length += 1
                if length > longest:
                    longest = length
        return longest


            

