


class Solution:
    def countBits(self, n: int) -> List[int]:
        
        dp = {0:0}
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i: #this offset finds the value with exactly 1 less 1-bit in it, and then adds 1. e.g
            # 15 and 7. 15 is all 1s. 7 is all 1s. But 15 is just the larger one with 1 more 1. 
            #We change offset when i goes to a larger 'magnitude' For example from 15-> 16 with offset 8, offset should now be 16.
                offset *= 2
            dp[i] = 1 + dp[i - offset]
        
        return list(dp.values())


