"""
We use a stack data structure.
This is recursion problem, I have identified this because there are nested structures witin the s.



"""


class Solution:
    def decodeString(self, s: str) -> str:
        
        res = []

        def recurse(index, number):
            cur = []
            while index < len(s) and s[index] != ']':
                if s[index].isdigit():
                    r = index
                    while r < len(s) and s[r].isdigit():
                        r+=1
                    recursion = recurse(r+1, int("".join(s[index:r])))  #skip the bracket following the integer
                    cur.append(recursion[0]) 
                    index = recursion[1] + 1
                else:
                    cur.append(s[index])
                    index += 1
            joined = "".join(cur)
            return (joined * number, index)

        return recurse(0, 1)[0]
        



            








