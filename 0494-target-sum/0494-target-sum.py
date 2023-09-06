class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        self.result = 0
        self.memo = {}
        def dfs(array, target, index):
            res1, res2 = 0, 0
            if ((target, index) in self.memo):
                return self.memo[(target, index)]
            # if target is zero and we have reached the end of array then that means we
            # found a match
            if (target == 0 and index == len(nums)):
                return 1
            # if target is not zero and we reached the end of array then that means
            # it is not a match
            if (index == len(nums)):
                return 0
            if (len(array) > 1):
                res1 = dfs(array[1::], target - array[1], index + 1)
                res2 = dfs(array[1::], target + array[1], index + 1)
            self.memo[(target, index)] = res1 + res2
            return res1 + res2
        
        a = dfs(nums, target - nums[0], 1)  
        b = dfs(nums, target + nums[0], 1)  
        return a + b