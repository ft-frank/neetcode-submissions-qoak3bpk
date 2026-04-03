class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        brackets = {

            '}':'{',
            ']':'[',
            ')':'(',
        }

        for bracket in s:

            if bracket in brackets:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if brackets[bracket] != top:
                    return False
            else:
                stack.append(bracket)


        return True if not stack else False