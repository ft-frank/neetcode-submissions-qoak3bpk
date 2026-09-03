class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32): #check all 32 bits
            bit = (n >> i) & 1 # right shift i by 1 more bit each iteration, and then take its lowest bit. right shift eliminates the lowest bit, so it does change
            res = res | bit << (31 - i) #left shift bit back to 32 bits long, so you can accuratily bitwose or it with res
        return res
