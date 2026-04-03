class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        n = len(nums) /2
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
            if freq[num] > n:
                return num