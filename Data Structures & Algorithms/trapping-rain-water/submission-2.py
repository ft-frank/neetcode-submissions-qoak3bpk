class Solution:
    def trap(self, height: List[int]) -> int:
        #WHAT AM I DOING WHY WOULD I DO STARTING FORM START. ONLY NEEDED TO PATTERNS OF SHAPE
        #I SHOULD BE DOING START AND END TWO POINTERS BRUHHHH
        if len(height) == 0:
            return 0
        l = 0
        r = len(height) - 1

        leftMax = height[l]
        rightMax = height[r]

        res = 0 #res stands for response

        while l < r:

            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            
            else: 
                r -=1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res




