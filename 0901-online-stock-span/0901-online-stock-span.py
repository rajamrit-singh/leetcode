class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        cur = 1
        while(len(self.stack) > 0 and price >= self.stack[-1][0]):
            cur += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, cur))
        return cur


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)