# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        smallest = root.val
        second = float('inf')
        def dfs(node):
            nonlocal smallest, second
            if not node:
                return
            curr = node.val
            if curr <= smallest:
                smallest = curr
            elif curr < second:
                second = curr
            
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        if second == float('inf'):
            return -1
        return second
            