class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while True:
            summation = numbers[l] + numbers[r]
            if summation == target:
                return [l+1, r+1]
            elif summation < target:
                l += 1
            else:
                r -= 1

            