# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new = TreeNode(val, left = root, right = None)
            return new 

        def dfs(node, d):
            if not node:
                return
            if depth == d + 1:
                l = node.left
                r = node.right
                node.left = TreeNode(val, left = l, right = None)
                node.right = TreeNode(val, left = None, right = r)
                return 
            dfs(node.left, d + 1)
            dfs(node.right, d + 1)
        dfs(root, 1)
        return root

                

