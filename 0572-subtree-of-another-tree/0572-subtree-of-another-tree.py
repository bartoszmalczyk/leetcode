# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def are_same(node, subnode):
            if not node and not subnode:
                return True
            elif not node or not subnode:
                return False
            
            if node.val != subnode.val:
                return False
            
            return (
                are_same(node.left, subnode.left) 
                and are_same(node.right, subnode.right)
            )

        def dfs(node):
            if not node:
                return False
            
            if node.val == subRoot.val and are_same(node, subRoot):
                return True

            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)