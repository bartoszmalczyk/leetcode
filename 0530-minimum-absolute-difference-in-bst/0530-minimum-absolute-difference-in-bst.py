# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = [] 
        ans = float('inf')
        def dfs(node):
            if not node:
                return
            arr.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        arr.sort()
        for i in range(0, len(arr) - 1):
            ans = min(ans, abs(arr[i + 1] - arr[i]))
        return ans
            