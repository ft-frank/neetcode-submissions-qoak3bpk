class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        #gets the digits in form to be able to be squared
        while True:
            digits = str(n)
            arr = list(digits)
            digits = [int(a) for a in arr]
            digits = [d**2 for d in digits] #squaring
            summation = sum(digits)
            if summation == 1:
                return True
            elif summation in seen:
                return False
            else:
                seen.add(n)
                n = summation

                


