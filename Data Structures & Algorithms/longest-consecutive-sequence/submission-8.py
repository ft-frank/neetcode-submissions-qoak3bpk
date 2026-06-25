class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        for n in nums:
            if n - 1 not in nums:
                count = 1
                while n + 1 in nums:
                    n += 1
                    count += 1
                if count > res:
                    res = count
        return res

                    
        