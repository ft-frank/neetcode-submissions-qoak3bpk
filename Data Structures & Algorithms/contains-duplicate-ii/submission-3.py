class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        

        l = 0
        length = len(nums)
        window = set()
    
        for r in range(length):
            
            if nums[r] in window:
                return True
            else:
                window.add(nums[r])
            if r - l + 1 > k:
                window.remove(nums[l])
                l +=1
        return False
            
            
            