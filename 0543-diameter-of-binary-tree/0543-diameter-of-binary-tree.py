# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
    def __init__(self):
        self.maxD = 0

    def diameterOfBinaryTree(self, root):
        self.diameter(root)
        return self.maxD - 1

    def diameter(self, root):
        if (root == None):
            return 0
        left = self.diameter(root.left)
        right = self.diameter(root.right)
        self.maxD = max(1 + left + right, self.maxD)
        return 1 + max(left, right)