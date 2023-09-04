class Solution:
    def maxProfit(self, prices) -> int:
        dp = {}


        def dfs(i, buying):
            if (i >= len(prices)):
                return 0
            if dp.get((i, buying)):
                return dp[(i, buying)]
            if (buying):
                buy = dfs(i + 1, False) - prices[i]
                cooldown = dfs(i + 1, True)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, True) + prices[i]
                cooldown = dfs(i + 1, False)
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        val = dfs(0, True)
        return val