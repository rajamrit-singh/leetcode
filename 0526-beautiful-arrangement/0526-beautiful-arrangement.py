class Solution(object):

    def __init__(self):
        self.result = []

    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n == 1):
            return 1
        nums = [i for i in range(1, n + 1)]
        self.dfs(nums, [], 1, [])
        print(self.result)
        return len(self.result)

    def dfs(self, nums, visited, ind, perm):
        if(len(perm) == len(nums)):
            self.result.append(perm[::])
        
        for i in range(0, len(nums)):
            if (nums[i] not in visited and (nums[i] % ind == 0 or ind % nums[i] == 0)):
                perm.append(nums[i])
                visited.append(nums[i])
                self.dfs(nums, visited, ind + 1, perm)
                perm.pop()
                visited.pop()
