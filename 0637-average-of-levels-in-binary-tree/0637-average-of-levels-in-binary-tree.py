from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        hm = defaultdict(list)
        def dfs(node,lvl):
            if not node: 
                return 
            hm[lvl].append(node.val)
            dfs(node.left, lvl + 1)
            dfs(node.right, lvl + 1)
        dfs(root, 0)
        ans = []
        sol = list(hm.values())
        for stage in sol:
            ans.append(sum(stage) / len(stage))
        return ans