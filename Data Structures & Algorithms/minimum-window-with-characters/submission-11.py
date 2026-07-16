"""
So close to independantly getting it. If I think the logic is correct, 
then check all the variables, and see if the
code I'm writing is actually what I'm thinking.
I just had to change two r's to two l's. And I solved 
it a long time ago.



"""



class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""
        
        second = {}
        for c in t:
            second[c] = second.get(c, 0) + 1
        
        #Creates a dictionary that counts the number of characters for each character in t 

        first = {}

        matches = 0 #counts the number of matches. Matches required would be length of t.
        matches_needed = len(second.keys())

        l, r = 0, 0
        res = ""
        res_length = float('inf')

        n = len(s)

        while r < n:
            if l == r and s[r] not in t:
                l, r = l + 1, r + 1
                continue
            first[s[r]] = first.get(s[r], 0) + 1
            if s[r] in t:
                if first[s[r]] == second[s[r]]:
                    matches += 1
                while s[l] not in second or first[s[l]] > second[s[l]]:
                    first[s[l]] -= 1
                    l += 1

                if matches == matches_needed:
                    length = r - l + 1
                    if length < res_length:
                        res = s[l:r+1]
                        res_length = length
            r += 1
        return res
                


