# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # using dfs 
        def dfs(node, mn, mx):
            # Node is Null or leaf node
            if (node is None) : 
                return True
            if not (node.val < mx and node.val > mn):
                return False
            
            return dfs(node.left, mn , node.val) and dfs(node.right, node.val , mx)
            
        return dfs(root, float(-inf) , float(inf))
        