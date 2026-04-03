class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        freqS1 = {}
        for letter in s1:
            freqS1[letter] = 1 + freqS1.get(letter, 0)
        
        freqWindow = {}
        for i in range(len(s1)):
            freqWindow[s2[i]] = 1 + freqWindow.get(s2[i], 0)


        for right in range(len(s1), len(s2)):
            left = right - len(s1)
            if freqWindow == freqS1:
                return True
            if freqWindow[s2[left]] > 1:
                freqWindow[s2[left]] -= 1
            else: 
                del freqWindow[s2[left]]
            freqWindow[s2[right]] = 1 + freqWindow.get(s2[right], 0)
        if freqWindow == freqS1:
                return True
        return False
        