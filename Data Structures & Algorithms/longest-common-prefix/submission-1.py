class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        minLen = 201
        for s in strs:
            minLen = min(len(s), minLen)
        valid = True
        i = 0
        s = 0
        ans = []
        while valid and i < minLen:
                if s > 0:
                    if strs[s][i] != strs[s - 1][i]:
                        valid = False
                
                if s == len(strs) - 1:
                    if valid:
                        ans.append(strs[0][i])
                    s = 0
                    i += 1
                    
                s += 1
        return "".join(ans)      
