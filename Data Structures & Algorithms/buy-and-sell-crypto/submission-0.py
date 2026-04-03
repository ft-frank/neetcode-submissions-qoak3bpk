class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        profit = 0
        for right in range(len(prices)):
            if prices[right] == prices[left]:
                continue
            elif prices[right] > prices[left]:
                gap = prices[right] - prices[left]
                profit = max(gap, profit)
            elif prices[left] > prices[right]:
                left = right
        return profit


            