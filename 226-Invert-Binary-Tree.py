class Solution:
     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
         temp = root
         def helper(root):
             if not root:
                 return None
             #elif not root.left or not root.right:
             #    return root
             else:
                 root.left, root.right = root.right, root.left
                 helper(root.left)
                 helper(root.right)
         helper(root)
         return temp