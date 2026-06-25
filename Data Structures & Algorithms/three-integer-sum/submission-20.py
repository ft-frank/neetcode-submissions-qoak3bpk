class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                target = -nums[i]
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    summation = nums[l] + nums[r]
                    if summation == target:
                        current = [nums[l], nums[r], nums[i]]
                        res.append(current)
                        l += 1
                        r -= 1
                        while nums[l-1] == nums[l] and l < r:
                            l += 1
                    elif summation < target:
                        l += 1
                    else:
                        r -= 1

        return res




                