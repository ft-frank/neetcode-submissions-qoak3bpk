class Solution:
    def validPalindrome(self, s: str) -> bool:
        def validatePalindrome(l , r):

            while l < r:

                if s[l] == s[r]:
                    r -= 1
                    l += 1
                else:
                    return False
            return True
        l = 0
        r = len(s) - 1

        while l < r:

            if s[l] == s[r]:
                r -= 1
                l += 1
            else:
                return validatePalindrome(l, r - 1) or validatePalindrome(l + 1, r)

        return True