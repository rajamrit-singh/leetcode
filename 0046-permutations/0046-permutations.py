class Solution(object):
    def __init__(self):
        self.result = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # for i in range(0, len(nums)):
        #     n = nums.pop(0)
        #     # Take recursive leap of faith and imagine that we get all the permutations here
        #     # for example if [2, 3] we get [[2,3], [3,2]]
        #     perms = self.permute(nums)
        #     # Next thing that we want to do is append n to all of these permutations
        #     # [[2, 3, 1], [3, 2, 1]]
        #     for perm in perms:
        #         # Append it at the end of all the permutations
        #         perm.append(n)
        #     nums.append
        length = len(nums)
        visited = [False] * length
        permutation = []
        def permuteArr(nums, perms):
            if (len(perms) == length):
                print(perms)
                self.result.append(perms[::])
                return
            for i in range(0, len(nums)):
                if (not visited[i]):
                    visited[i] = True
                    perms.append(nums[i])
                    permuteArr(nums, perms)
                    perms.pop()
                    visited[i] = False
        permuteArr(nums, [])
        print(self.result)
        return self.result
