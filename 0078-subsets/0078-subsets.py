class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        if (len(nums) == 0):
            return [[]]
        self.getSubsets(nums, [], 0)
        return self.result
    
    
    def getSubsets(self, nums, path, cur):
        if(cur == len(nums)):
            self.result.append(path)
            return
        
        self.getSubsets(nums, path + [nums[cur]], cur + 1)
        self.getSubsets(nums, path, cur + 1)