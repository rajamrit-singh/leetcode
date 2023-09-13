class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minimum = min(nums)
        maximum = max(nums)
        cur = minimum
        while (cur > 1):
            if (maximum % cur == 0 and minimum % cur == 0):
                return cur
            cur -= 1
        return 1