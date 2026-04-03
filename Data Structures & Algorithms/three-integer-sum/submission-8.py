from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        sortedNums = nums.sort() 

        for i, num in enumerate(nums):  
            if i > 0 and num == nums[i-1]:
                continue
            else:
                l = i + 1
                r = len(nums) - 1
                target = 0 - (num)
                while l < r:
                    summation = nums[l] + nums[r]
                    if summation == target:
                        output.append([num, nums[l], nums[r]]) 
                        l += 1
                        while l < r and nums[l-1] == nums[l]:
                            l+=1
                        r -= 1
                        while l < r and nums[r + 1] == nums[r]:
                            r-=1
                    elif summation < target:
                        l += 1
                    elif summation > target:
                        r -= 1
        return output

#example [-2, 0, 0 , 2 ,2]