class Solution:

    def __init__(self):
        self.denominations = float("inf")
        self.memo = {}

    def coinChange(self, coins, amount):
        if (amount == 0):
            return 0

        def dfs(cns, target):
            if (target < 0):
                return -1
            if(self.memo.get(target)):
                return self.memo[target] + 1
            if (target == 0):
                return 1
 
            curDenom = float("+inf")
            for i in cns:
                res = dfs(cns, target - i)
                if(res > 0 and res < curDenom):
                    curDenom = res
            self.memo[target] = curDenom
            return curDenom + 1
            
        dfs(coins, amount)
        print(self.memo)
        if (self.memo[amount] != float("+inf")):
            return self.memo[amount]
        return -1