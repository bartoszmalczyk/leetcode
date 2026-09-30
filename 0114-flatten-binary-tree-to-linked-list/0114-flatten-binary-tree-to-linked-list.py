# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node:
                return 
            if node.left:
                temp = node.right
                node.right = node.left
                node.left = None

                x = node.right
                while x.right:
                    x = x.right
                    
                x.right = temp 
            dfs(node.right)
        dfs(root)
            
            
            
