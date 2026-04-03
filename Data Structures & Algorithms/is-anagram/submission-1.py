class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        The number of each letters has to equal the number of each letter in the other one.
        -> Some sort of linear search
        Another solution, is if I sort the things does it equal? -> not optimal
        time complexity would be O(n logn * 2)
        """
        s_map = {}
        t_map = {}

        for letter in s:
            if letter not in s_map:
                s_map[letter] = 1
            else:
                s_map[letter] += 1 

        for letter in t:
            if letter not in t_map:
                t_map[letter] = 1
            else:
                t_map[letter] += 1 

        if s_map == t_map: 
            return True
        else: 
            return False
