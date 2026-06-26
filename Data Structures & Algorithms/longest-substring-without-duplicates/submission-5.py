class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        
        max_length = 0
        seen = set()
        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                max_length = max(len(seen), max_length)
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
        return max_length

            

