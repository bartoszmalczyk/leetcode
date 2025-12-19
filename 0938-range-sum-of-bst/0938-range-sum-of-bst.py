# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = [0]
        def dfs(node):
            if not node: return
            if node.val < low:
                dfs(node.right)
            elif node.val > high:
                dfs(node.left)
            else:
                dfs(node.right)
                dfs(node.left)
                ans[0] += node.val

        dfs(root)
        return ans[0]
        