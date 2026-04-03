class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if len(tokens) < 3:
            return int(tokens[0])
        stack = []

        operators = {
            "+", "/", "*", "-"
        }
        def eval(v1, v2, operator):
            if operator == "+":
                return add(v1, v2)
            elif operator == "-":
                return subtract(v1, v2)
            elif operator == "/":
                return divide(v1, v2)
            elif operator == "*":
                return multiply(v1, v2)
        
        def add(v1, v2):
            return v1 + v2
        def multiply(v1, v2):
            return v1 * v2
        def subtract(v1, v2):
            return v2 - v1
        def divide(v1, v2):
            return int(v2 / v1)

        for token in tokens:
            if token in operators:
                v1 = stack.pop()
                v2 = stack.pop()
                newVal = eval(v1, v2, token)
                stack.append(newVal)
            else:
                stack.append(int(token))
        return stack[0]


