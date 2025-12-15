# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        height = [-1]
        ans = []
        def dfs(node, curr_height):
            if not node:
                return
            if curr_height > height[0]:
                ans.append(node.val)
                height[0] = curr_height
            dfs(node.right, curr_height + 1)
            dfs(node.left, curr_height + 1)
        dfs(root,0)
        return ans
            