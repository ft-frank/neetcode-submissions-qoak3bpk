class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsFound = set()
        for num in nums:
            if num in numsFound:
                return True
            else:
                numsFound.add(num)
        return False

        
        
        

        