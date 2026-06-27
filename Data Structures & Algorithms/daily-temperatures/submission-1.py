class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            new = []
            while len(stack) > 0 and t > temperatures[stack[-1]]: 
                index = stack.pop()
                difference = i - index
                res[index] = difference
            stack.append(i)
        return res
                