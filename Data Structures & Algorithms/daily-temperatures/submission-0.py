class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =[]
        res = []


        p = len(temperatures) - 1

        for i in range(len(temperatures)):
            if not stack:
                stack.append((temperatures[p], i)) #tuple: (temperatureValue, index P)
                res.append(0)
            elif temperatures[p] < stack[-1][0]:
                diffDays = i - stack[-1][1]
                stack.append(   (temperatures[p], i) )
                res.append(diffDays)
            else:
                while len(stack) > 0 and temperatures[p] >= stack[-1][0]:
                    stack.pop()
                if len(stack) == 0:
                    res.append(0)

                else: 
                    diffDays = i - stack[-1][1]
                    res.append(diffDays)
                stack.append((temperatures[p], i) )
            p -= 1
        res.reverse()
        return res