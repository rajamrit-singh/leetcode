class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 1):
            return nums[0]
        length = len(nums)
        return max(self.houseRobber(nums[1: :]), self.houseRobber(nums[0:length - 1:]))
        
    
    def houseRobber(self, arr):
        cur = 0
        prior = 0
        prev = 0
        for num in arr:
            cur = max(num + prior, prev)
            prior = prev
            prev = cur
        return cur