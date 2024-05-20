# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if (root == None):
            return root
        stack = []
        result = []
        # stack.append(root)
        node = root
        stack.append(node)
        node = node.left
        while (len(stack) > 0 or node != None):
            if (node == None):
                node = stack.pop()
                result.append(node.val)
                node = node.right
                continue
            if (node.left):
                stack.append(node)
                node = node.left
            else:
                result.append(node.val)
                node = node.right
                
        return result