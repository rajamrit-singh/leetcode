class Solution:

    def __init__(self):
        self.result = 0
        self.memo = {}

    def change(self, amount: int, coins) -> int:
        if (amount == 0):
            return 1

        def dfs(coins, amt, index):
            if (amt < 0):
                return 0
            if (amt == 0):
                return 1
            if ((amt, index) in self.memo):
                return self.memo.get((amt, index))


            total = 0

            for i in range(index, len(coins)):
                # We are passing the index so that in we don't get repitions
                a = dfs(coins, amt - coins[i], i)
                total += a
            self.memo[(amt, index)] = total
            return total
        return dfs(coins, amount, 0)
        # answer = self.memo.get((amount, 0)) or 0
        # return answer