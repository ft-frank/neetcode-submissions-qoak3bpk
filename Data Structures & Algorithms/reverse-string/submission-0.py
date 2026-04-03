class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) -1

        while l < r:
            temporaryL = s[l]
            temporaryR = s[r]
            s[l] = temporaryR
            s[r] = temporaryL
            r -= 1
            l += 1
