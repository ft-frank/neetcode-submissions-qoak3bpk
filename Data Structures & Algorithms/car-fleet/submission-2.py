class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        fleets = 0
        
        hashMap = {}
        if len(position) == 1:
            return 1

        fleet = 0
        for i in range(len(position)):
            pos = position[i]
            speeds = speed[i]
            hashMap[pos] = speeds
        position.sort(reverse = True)

        currentSlowest = 0
        for i in range(len(position)):
            pos = position[i] #starting at furthest away
            speed = hashMap[pos]
            time_to_target = ((target - pos) / speed)
            if len(stack) > 0 and time_to_target > stack[0]:
                stack = []
                fleet += 1
            stack.append(time_to_target)
        
        return fleet + 1



        