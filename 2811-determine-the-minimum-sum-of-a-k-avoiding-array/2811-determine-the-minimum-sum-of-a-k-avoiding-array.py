class Solution(object):
    def minimumSum(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        myDict = {}
        ptr = 0
        num = 1
        result = []
        while(ptr < n):
            comp = k - num
            if (myDict.get(comp)):
                num += 1
                continue
            else:
                result.append(num)
                myDict[num] = True
                ptr += 1
                num += 1
        return sum(result)