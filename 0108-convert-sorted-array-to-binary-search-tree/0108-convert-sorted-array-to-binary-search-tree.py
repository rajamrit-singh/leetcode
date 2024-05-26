# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.getHeightBalancedTree(nums)
    
    def getHeightBalancedTree(self, nums):
        if (len(nums) == 0):
            return None
        mid = math.floor(len(nums) / 2)
        root = TreeNode(nums[mid])
        root.left = self.getHeightBalancedTree(nums[:mid])
        root.right = self.getHeightBalancedTree(nums[mid + 1::])
        return root