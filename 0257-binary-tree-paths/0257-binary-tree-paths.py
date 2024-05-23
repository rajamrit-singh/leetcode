# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.result = []
        self.stack = []
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.getAllPaths(root)
        finalResult = ["->".join(map(str, i)) for i in self.result]
        return finalResult
    
    def getAllPaths(self, root):
        if (root == None):
            return
        self.stack.append(root.val)
        self.getAllPaths(root.left)
        self.getAllPaths(root.right)
        if (not root.left and not root.right):
            self.result.append(self.stack.copy())
        self.stack.pop()