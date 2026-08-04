"""
We can use a sliding window approach, that attempts to create the largest valid window, and then once can't extend any longer, records length
and then resets window.


For example 2:


"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        res = 1
        seen = {}
        top_frequency = 0

        while r < len(s):
            char = s[r]
            seen[char] = seen.get(char, 0) + 1 #we have seen this char
            top_frequency = max(top_frequency, seen[char])  #we find max top_frequency

            #r - l + 1 - top_frequncy must be max k, any more than k we have to remove characters

            while r-l+1-top_frequency > k:
                remove = s[l]
                seen[remove] -=1

                #how to adjust top_frequency?
                l+=1
            res = max(r-l+1, res)
            r += 1

        return res






    
            
