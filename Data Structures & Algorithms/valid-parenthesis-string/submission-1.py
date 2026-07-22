class Solution:
    def checkValidString(self, s: str) -> bool:
        
        min_open = 0 #the minimum number of brackets I have open at the moment
        max_open = 0 #the maximum . The difference between the two is the *


        for c in s:
            
            if c == "(":
                min_open += 1
                max_open += 1
            elif c == ")":
                min_open -= 1
                max_open -= 1
            elif c == "*":
                min_open -= 1
                max_open += 1
            
            #return false if statements
            if min_open < 0:
                min_open = 0
            if max_open < 0:
                return False

        return min_open == 0
                