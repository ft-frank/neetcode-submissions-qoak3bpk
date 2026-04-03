class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0

        length = len(nums)
    
        currentSum = 0
        sumLen = float("Infinity")

        for r in range(length):
            currentSum += nums[r]

            while currentSum >= target:
                sumLen = min(r - l + 1, sumLen)
                currentSum -= nums[l]
                l += 1

        return sumLen if sumLen != float("infinity") else 0

        