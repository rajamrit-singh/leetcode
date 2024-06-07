class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if (len(nums) == 0 or sum(nums) == 0):
            return "0"
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                num1 = str(nums[i]) + str(nums[j])
                num2 = str(nums[j]) + str(nums[i])
                if (int(num2) > int(num1)):
                    nums[i], nums[j] = nums[j], nums[i]
        res = ""
        for num in nums:
            res += str(num)
        return res