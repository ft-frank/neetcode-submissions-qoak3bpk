class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        if digits[-1] != 10:
            return digits
        
        res = []
        remainder = 0
        for i in range(len(digits)-1, -1, -1):
            val = digits[i]
            dig = val + remainder
            if dig == 10:
                res.append(0)
                remainder = 1
            else:
                res.append(dig)
                remainder = 0

        if remainder:
            res.append(1)
    
        res.reverse()
        return res