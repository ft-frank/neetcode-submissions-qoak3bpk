class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0 
        r = len(heights) - 1
        largest = 0

        def area(h1, h2, length):
            height = min(h1, h2)
            return length * height
        while l < r:
            if area(heights[l], heights[r], r - l) > largest:
                largest = area(heights[l], heights[r], r - l)
            if heights[l] > heights[r]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1
            else:
                l += 1
                r -= 1
        return largest

                
