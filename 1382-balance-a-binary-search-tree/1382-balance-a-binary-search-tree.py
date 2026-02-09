# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        values = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)
        dfs(root)
        l = 0 
        r = len(values) -1
        tree = TreeNode()
        def build(left, right):
            if left > right: 
                return None
            mid = (left + right) // 2
            node = TreeNode(values[mid])
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)
            return node 
        return build(l, r)
