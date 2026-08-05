
"""
We extended window until we get all characers needed.
Shorten as much as possible. 
Record length. 


"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l = r = matches = 0
        res = ""
        res_length = float('inf')
        str1 = {}
        str2 = {}

        if len(t) > len(s):
            return res

        for c in t:
            str1[c] = str1.get(c, 0) + 1 #count characters within t
        matches_needed = len(str1.keys()) #count how many characters we have to match


        while r < len(s): #while we can keep extending our window
            new_c = s[r]
            str2[new_c] = str2.get(new_c, 0) + 1 #adding a new character to Window

            if new_c in str1 and str1[new_c] == str2[new_c]:
                matches += 1 #if we match a character, then add to matches.


            if matches == matches_needed: # if we have enough matches
                while matches == matches_needed: #remove all characters that aren't needed to represent t
                    
                    #Save current res, then remove the left one to try reduce size
                    if res_length > r - l + 1: #  if size of window 
                       res_length = r - l + 1 
                       res = s[l:r+1] 

                    old_c = s[l] #remove the front of the window
                    if old_c in str1 and str1[old_c] == str2[old_c]:
                        matches -= 1    
                    str2[old_c] -= 1
                    l += 1
                    

        
            r+= 1
        return res


           

        
        