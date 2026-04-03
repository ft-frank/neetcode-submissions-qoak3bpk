from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums) # O(n)

        counter = 0

        alrSearched = set() # O(1) lookup
        count = 1
        process = True
        for num in nums: #O(n) time, So far # O(n) space complexity, because of the nums being an array
            if num in alrSearched:
                process = False
            else: process = True
            while process:
                num += 1
                alrSearched.add(num)
                if num in nums: #O (1) lookup
                    count += 1
                else:
                    if count > counter:
                        counter = count
                    count = 1
                    process = False
        return counter                
                
            


            

