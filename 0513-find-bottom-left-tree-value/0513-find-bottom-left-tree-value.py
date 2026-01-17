# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = (root.val, 0)
        def dfs(node, lvl):
            nonlocal ans
            if not node: return
            if lvl > ans[1]:
                ans = (node.val, lvl)
            dfs(node.left, lvl + 1)
            dfs(node.right, lvl + 1)
        dfs(root, 0)
        return ans[0]