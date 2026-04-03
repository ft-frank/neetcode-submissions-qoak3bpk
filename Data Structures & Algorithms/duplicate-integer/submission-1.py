class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsFound = []
        for num in nums:
            if num in numsFound:
                return True
            else:
                numsFound.append(num)
        return False

        
        
        

        