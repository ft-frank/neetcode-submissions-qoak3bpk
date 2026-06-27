class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'*', '/', '+', '-'}
        for t in tokens:
            if t not in operators:
                stack.append(t)
            else:
                second = int(stack.pop())
                first = int(stack.pop())
                if t == "+":
                    result = first + second
              
                elif t == "-":
                    result = first - second
                  
                elif t == "*":
                    result = first * second
             
                elif t == "/":
                    result = int(first /second)
                stack.append(result)

        res = stack[0]
        return int(res)