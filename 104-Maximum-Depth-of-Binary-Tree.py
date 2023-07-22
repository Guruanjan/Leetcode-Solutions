# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if node is None:
                return 0 
            if node.left is None and node.right is None:
                return 1 
            if node.left is None and node.right:
                return 1 + depth(node.right)
            
            if node.left and node.right is None:
                return 1 + depth(node.left)
            return max(depth(node.left) + 1 , depth(node.right) + 1)
        return depth(root)
        