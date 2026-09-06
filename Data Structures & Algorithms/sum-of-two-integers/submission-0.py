class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF # 32-bit integer
        max_int = 0x7FFFFFFF #32-bit integer

        while b != 0:               
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= max_int else ~(a ^ mask)


        