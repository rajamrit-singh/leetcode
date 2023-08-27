class Solution(object):
    def minimumPossibleSum(self, n, target):
        """
        :type n: int
        :type target: int
        :rtype: int
        """
        arr = []
        numCount = 1
        myHash = {}
        while (len(arr) != n):
            # if (numCount > 10000):
            #     return
            rem = target - numCount
            if(myHash.get(rem)):
                numCount += 1
                continue
            myHash[numCount] = True
            arr.append(numCount)
            numCount += 1
        print(arr)
        return sum(arr)
        