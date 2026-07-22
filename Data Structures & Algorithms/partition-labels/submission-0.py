class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        res = []

        last = {}

        for i in range(len(s) - 1, -1, -1): #finds the index of the last found character of a string
            if s[i] not in last:
                last[s[i]] = i

        
        size = 0
        seen = set()
        finished = 0

        for i, c in enumerate(s):
            seen.add(c)
            size += 1
            if last[c] == i:
                finished += 1
            if finished == len(seen):
                res.append(size)
                size = 0
                seen = set()
                finished = 0


        return res


"""
We keep track of characters we have seen
x, y, x, x,y. Boom we have caught all x and y, therefore it is recommended we stop here, as we can start another array.

z, b, z, b, b. Boom we have caught all z and b. We can start antoher string, because no other string will contain z and b, which ensures that each letter appears in at most one substring.

i, we have caught all i. 



"""