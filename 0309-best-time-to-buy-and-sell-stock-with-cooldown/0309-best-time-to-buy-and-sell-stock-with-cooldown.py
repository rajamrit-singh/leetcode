class Solution:
    def maxProfit(self, prices) -> int:
        dp = {}  # dictionary to store previously computed results
        
        def dfs(i, buying):
            if (i >= len(prices)):
                return 0  # base case: if we have reached the end of the prices array, return 0
            if dp.get((i, buying)):
                return dp[(i, buying)]  # if the result for this state has already been computed, return it
            if (buying):
                buy = dfs(i + 1, False) - prices[i]  # if we are buying, we can either buy the stock or cooldown
                cooldown = dfs(i + 1, True)
                dp[(i, buying)] = max(buy, cooldown)  # store the maximum profit in the dp dictionary
            else:
                sell = dfs(i + 2, True) + prices[i]  # if we are selling, we can either sell the stock or cooldown
                cooldown = dfs(i + 1, False)
                dp[(i, buying)] = max(sell, cooldown)  # store the maximum profit in the dp dictionary
            return dp[(i, buying)]  # return the maximum profit for this state
        
        val = dfs(0, True)  # start the recursive function from the first day with buying as True
        return val  # return the maximum profit