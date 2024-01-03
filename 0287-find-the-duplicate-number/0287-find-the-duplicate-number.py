class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while (True):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if (slow == fast):
                break
        newSlow = nums[0]
        while (newSlow != slow):
            newSlow = nums[newSlow]
            slow = nums[slow]
        return slow