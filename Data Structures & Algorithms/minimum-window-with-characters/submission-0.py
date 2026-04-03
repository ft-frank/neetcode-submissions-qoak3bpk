class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        window = {}
        tCount = {}
        
        output = []

        for letter in t:
            tCount[letter] = 1 + tCount.get(letter, 0)
        
        res, resLen = [0, 0], float("infinity")
        matches = 0
        n = len(tCount)
        l = 0 
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in tCount and window[c] == tCount[c] : #ohhh had to think more logically bruh
                matches += 1
            
            while matches == n:
                if r - l + 1 < resLen:              #r - l + 1 is a common pattern to determine sliding window length
                     res = [l, r]
                     resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in tCount and window[s[l]] < tCount[s[l]]: 
                    matches -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float("infinity") else ""        
            

            
        

        
        
        