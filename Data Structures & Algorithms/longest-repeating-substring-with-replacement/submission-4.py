class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        longest = 1
        seen = {}
        top_frequency = 0
        while r < len(s):
            seen[s[r]] = seen.get(s[r], 0) + 1
            top_frequency = max(top_frequency, seen[s[r]])
            while r - l + 1 - top_frequency > k:
                seen[s[l]] -= 1
                top_frequency = max(top_frequency, seen[s[l]])
                l += 1
            longest = max(longest, r-l+1)
            r += 1
        return longest

            
            

                