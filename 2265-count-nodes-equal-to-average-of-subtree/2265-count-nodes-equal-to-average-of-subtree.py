from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return [0,0]
            left = dfs(node.left)
            right = dfs(node.right)    
            val, ammount = left[0] + right[0], left[1] + right[1]
            ammount += 1
            val += node.val
            print(val, ammount)
            print("")
            if val // ammount == node.val:
                ans += 1
            return [val, ammount]
        dfs(root)
        return ans