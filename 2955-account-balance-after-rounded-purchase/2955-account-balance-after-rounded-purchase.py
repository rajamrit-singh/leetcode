class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        """
        :type purchaseAmount: int
        :rtype: int
        """
        if (purchaseAmount % 10 >= 5):
            while(purchaseAmount % 10 != 0):
                purchaseAmount += 1
        elif (purchaseAmount % 10 < 5):
            while(purchaseAmount % 10 != 0):
                purchaseAmount -= 1
        return 100 - purchaseAmount