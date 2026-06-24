from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list) #a dictionary full of empty keys with empty list values
        res = []
        for s in strs:

            count = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                count[index] += 1
            count = tuple(count)
            hashMap[count].append(s)
        for str_list in hashMap.values():
            res.append(str_list)
        return res

