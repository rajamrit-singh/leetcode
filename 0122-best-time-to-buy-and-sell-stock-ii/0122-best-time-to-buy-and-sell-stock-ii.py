class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        curProfit = float("-inf")
        # Here the idea is any day I earn a profit, I will sell it.
        #If price goes down, then new price is considered as buy price
        for i in range(1, len(prices)):
            curProfit = prices[i] - buy
            if (curProfit > 0):
                profit += curProfit
            buy = prices[i]
        return profit