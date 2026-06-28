class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
    
        l = 0
        r = len(s1) - 1
        first = [0] * 26
        second = [0] * 26

        if len(s1) > len(s2):
            return False

        for c in s1:
            index = ord(c) - ord('a')
            first[index] += 1

        for i in range(len(s1)):
            index = ord(s2[i]) - ord('a')
            second[index] += 1


        while r < len(s2)- 1:
            if first == second:
                return True
            else:
                index = ord(s2[l]) - ord('a')
                second[index] -= 1
                l += 1

                r += 1
                index = ord(s2[r]) - ord('a')
                second[index] += 1

        if first == second:
                return True
        return False
            

        
            
        