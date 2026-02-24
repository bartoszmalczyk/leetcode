# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node, lvl):
            if not node:
                return
            if len(ans) == lvl:
                ans.append(node.val)
            else:
                ans[lvl] = max(ans[lvl], node.val)
            dfs(node.left, lvl + 1)
            dfs(node.right, lvl + 1)
        dfs(root, 0)
        return ans