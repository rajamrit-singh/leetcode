class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if (amount == 0):
            return 1
        dp = [0 for i in range(0, amount + 1)]
        row = [0 for i in range(0, amount + 1)]
        # We will follow a bottom up approach 
        for i in range(len(coins) - 1, -1, -1):
            dp = row[::]
            # We only need the data from below row. Once we have passed a row
            # it will become the dp for next row
            for curAmt in range(1, amount + 1, 1):
                amt = curAmt - coins[i]
                if (amt < 0):
                    row[curAmt] = 0
                elif (amt == 0):
                    row[curAmt] = 1
                else:
                    row[curAmt] = row[amt]
                row[curAmt] += dp[curAmt]

        return row[amount]