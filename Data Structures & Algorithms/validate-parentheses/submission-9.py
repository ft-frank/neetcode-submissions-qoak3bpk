class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        valid_parentheses = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c in valid_parentheses:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if valid_parentheses[c] != top:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

        


