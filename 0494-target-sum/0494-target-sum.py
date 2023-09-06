class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        self.result = 0
        self.memo = {}
        def dfs(array, target, index):
            res1, res2 = 0, 0
            if ((target, index) in self.memo):
                return self.memo[(target, index)]
            if (target == 0 and index == len(nums)):
                return 1
            if (target < 0 and index == len(nums)):
                return 0
            if (len(array) > 1):
                res1 = dfs(array[1::], target - array[1], index + 1)
                res2 = dfs(array[1::], target + array[1], index + 1)
            self.memo[(target, index)] = res1 + res2
            return res1 + res2
        
        a = dfs(nums, target - nums[0], 1)  #3
        b = dfs(nums, target + nums[0], 1)  #2
        return a + b