class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lis = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                if(nums[i] < nums[j]):
                    lis[i] = max(lis[i], 1 + lis[j])
        return max(lis)