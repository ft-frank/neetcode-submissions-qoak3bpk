"""
Example 1:

asteroids = [2, 4, -4, 1]

Because 4 and -4 are in the opposite direction, they meet and collide. 
Since in [2, -1], 2 > 1, the 1 asteroid gets destroyed, leaving the one left.


Algorithm:

1. We use a LIFO stack
2. We add each asteroid in-order.
3. We compare each asteroid with the latest asteroid in the stack
4. If the right asteroid is less than the left asteroid, and different sign then compare futher
5. If same magnitude remove both, if different magnitude remove the one that is smaller


"""


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if len(stack) == 0:
                stack.append(a)
                continue
            broken = False
            while len(stack) > 0 and a < stack[-1] and a * stack[-1] < 0: #check if the right one is smaller than, and in opposite direction from. Continue breaking down asteroids
                if abs(a) == abs(stack[-1]): # a is less than stack[-1] BUT has same magnitude
                    stack.pop()
                    broken = True
                    break #both asteroids destroyed
                elif abs(a) > abs(stack[-1]): #we destroy the asteroid on top of stack, keep comparing
                    stack.pop()
                else:
                    #the asteroid we are on right now is broken
                    broken = True
                    break
            if not broken:
                stack.append(a)
                    

            #above, we run a while loop that pops until we can put in our asteroid. We can put in our asteroid when 


        return stack
            


