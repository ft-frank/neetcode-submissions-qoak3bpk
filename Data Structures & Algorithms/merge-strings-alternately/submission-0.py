class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        finalWord = []
        minLen = min(len(word1), len(word2))

        for i in range(minLen):
            finalWord.append(word1[i])
            finalWord.append(word2[i])
        if len(word1) > len(word2):
            for i in range(len(word2), len(word1)):
                finalWord.append(word1[i])
        if len(word2) > len(word1):
            for i in range(len(word1), len(word2)):
                finalWord.append(word2[i])
        return "".join(finalWord)