class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        if(len(nums) <= 1):
            return [nums[::]]
        for i in range(len(nums)):
            n = nums.pop(0)
            permutations = self.permuteUnique(nums)
            final = []
            for perm in permutations:
                perm.append(n)
                if (perm not in result):
                    final.append(perm)
            nums.append(n)
            
            result.extend(final)
        return result