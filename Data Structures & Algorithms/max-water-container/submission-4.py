class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        best = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            best = max(area, best)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return best