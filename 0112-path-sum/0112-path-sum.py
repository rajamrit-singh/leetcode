# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.sumExist = False
        self.targetSum = targetSum
        self.checkSum(root, 0)
        return self.sumExist
    
    def checkSum(self, root, cur):

        if (root == None):
            return None
        cur += root.val
        self.checkSum(root.left, cur)
        self.checkSum(root.right, cur)
        if (not root.left and not root.right and not self.sumExist):
            self.sumExist = cur == self.targetSum
            # if (self.sumExist):
            #     return