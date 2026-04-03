from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for letter in string:
                count[ord(letter) - ord("a")] += 1
            count = tuple(count)
            hashMap[count].append(string)
        outputss = []
        for listOfStrings in hashMap.values():
            outputss.append(listOfStrings)
        return outputss
            

