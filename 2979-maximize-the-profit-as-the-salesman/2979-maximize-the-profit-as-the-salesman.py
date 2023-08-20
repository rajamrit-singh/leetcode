class Solution(object):
    def maximizeTheProfit(self, n, offers):
        """
        :type n: int
        :type offers: List[List[int]]
        :rtype: int
        """
        sorted_offers = sorted(offers, key=lambda x: x[1])
        myArr = n*[0]
        for index, offer in enumerate(sorted_offers):
            init = offer[0]
            end = offer[1]
            
            #This will get us the maximum offer that we could have obtained before the 
            #range of houses for current offer
            if (init > 0):
                previousOffersSum = myArr[init - 1]
            else:
                previousOffersSum = 0
                
            # Maximum amount at the stage would be the amount from current offer 
            # plus the amount from offers before this range starts
            
            currentOfferSum = previousOffersSum + offer[2]
            
            # If this offer is better than the previous offer for this range then update it
            
            myArr[end] = max(myArr[end], currentOfferSum)

            if(index + 1 < len(sorted_offers)):
                next = sorted_offers[index + 1]
                nextStart = next[1]
                # After the last house in this offer range, the max I can earn is 
                # max(myArr[end], currentOfferSum) so now when we are looking for the
                # max gold in the next offer
                # we only have to do myArr[init - 1]

                for i in range(end, nextStart + 1):
                    myArr[i] = myArr[end]
            
        return max(myArr)