"""
Stack (onepass).

We create a monotonically increasing stack.

We append and append.

When we encounter a bar that is shorter than the bar on the top of the stack,
pop that bar, and take the difference between the recently encountered bar, and the next remaining bar on the stack.

This will give the area of the rectangle. 

Also consider the height of the rectangle.

"""



class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        stack = []
        res = 0

        for i, h in enumerate(heights):
            if len(stack) == 0 or h >= stack[-1][1]:
                stack.append((i, h))
                continue

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                rectangle = (i - index) * height
                res = max(rectangle, res)
                saved = index
            
            stack.append((saved, h))

        while stack:
            index, height = stack.pop()
            rectangle = (len(heights) - index) * height
            res = max(rectangle, res)


        return res


            
            
            
            





                