"""
Our algorithm can use a monotonically decreasing stack. 


"""

from collections import deque

class StockSpanner:

    def __init__(self):
        self.stack = []


    def next(self, price: int) -> int:
        if len(self.stack) == 0:
            self.stack.append((price, 1))
            return 1
        span = 1 #to include self
        while self.stack and price >= self.stack[-1][0]:
            prev = self.stack.pop()
            span += prev[1] #add the span on top

        self.stack.append((price, span))
        return span



        






        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)