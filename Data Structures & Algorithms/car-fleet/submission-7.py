class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []  
        # I have to sort by position in descending order

        n = len(position)

        res = 0
        position_speed = sorted([(position[i], speed[i]) for i in range(n)], reverse = True)
        times = [(target - item[0]) / item[1] for item in position_speed]
        for t in times:
            if len(stack) == 0:
                stack.append(t)
                res +=1
            elif t > stack[-1]:
                stack.append(t)
                res += 1
   
        return res



