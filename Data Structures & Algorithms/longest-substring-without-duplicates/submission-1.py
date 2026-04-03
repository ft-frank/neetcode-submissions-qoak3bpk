class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        sequence = set()
        #string concactenation creates a new string, so maybe use an array here. This array depends on the longest sequence. Therefore O(m) space complexity
        for right in range(len(s)):
            if s[right] not in sequence:
                sequence.add(s[right])
                longest = max(longest, len(sequence))
            else:
                while s[right] in sequence:
                    sequence.remove(s[left])
                    left += 1
                sequence.add(s[right])
        return longest
            