from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        sortedNums = nums.sort() # timsort O(n log n)
        #two pointers is O(n) time, and a for loop is O(n). Therefore desired O(n^2)
        hashMap = {}
        for i, num in enumerate(nums):
            if num in hashMap:
                continue
            else:    
                l = i + 1
                r = len(nums) - 1
                target = 0 - (num)
                while l < r:
                    summation = nums[l] + nums[r]
                    if summation == target:
                        if tuple([nums[l],nums[r],num]) not in hashMap:
                            output.append([nums[l],nums[r],num]) #tuple()
                            hashMap[tuple([nums[l],nums[r],num])] = "bruh"
                        l += 1
                        r -= 1
                    elif summation < target:
                        l += 1
                    elif summation > target:
                        r -= 1
        return output
                


    """
        I need to somehow use mathematics to eliminate possibilities.
        Because if i check every combination it ends up being factorials and stuff



        two pointers
        is it either opposite direction or same direciton?
        i reckon opposite direction



    """