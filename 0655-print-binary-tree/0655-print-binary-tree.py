# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        height = 0
        def dfs(node, lvl):
            nonlocal height
            if not node: return
            else:
                height = max(height,lvl)
            dfs(node.left, lvl + 1)
            dfs(node.right, lvl + 1)
        dfs(root, 0)

        res = []
        n = 2**(height + 1) - 1
        res = [[""] * n for _ in range(height + 1)]

        def dfs_placement(node, r,c):
            res[r][c] = str(node.val)
            if node.left:
                dfs_placement(node.left, r + 1, c - 2**(height - r - 1))
            if node.right:
                dfs_placement(node.right, r + 1, c + 2**(height - r - 1))
        
        dfs_placement(root, 0, (n - 1) // 2)
        return res
            
        