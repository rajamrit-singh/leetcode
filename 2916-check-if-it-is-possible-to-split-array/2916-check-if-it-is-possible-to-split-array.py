class Solution(object):
    def canSplitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: bool
        """
        # curSum = sum(nums)
        # while(len(nums) > 2):
        #     first = nums[0]
        #     last = nums[-1]
        #     firstRemovedSum = curSum - first
        #     lastRemovedSum = curSum - last
        #     if (firstRemovedSum >= m):
        #         nums = nums[1::]
        #         curSum = curSum - first
        #     elif (lastRemovedSum >= m):
        #         lastIndex = len(nums)
        #         nums = nums[:lastIndex - 1:]
        #         curSum = curSum - last
        #     else:
        #         return False
        # return True
        if (len(nums) <= 2):
            return True
        length = len(nums)
        for (index, value) in enumerate(nums):
            if(index == len(nums) - 1):
                break
            if(value + nums[index + 1] >= m):
                return True
        return False
