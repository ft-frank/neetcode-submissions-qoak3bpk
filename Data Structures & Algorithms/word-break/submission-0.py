


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}
        n = len(s)

        def match(i):
            if i in memo:
                return memo[i]
            if i >= n:
                return True
            res = False
            for word in wordDict:
                length = len(word)
                if i + length <= n and s[i:i+length] == word:
                    res = res or match(i + length)
            memo[i] = res
            return memo[i]

        return match(0)

