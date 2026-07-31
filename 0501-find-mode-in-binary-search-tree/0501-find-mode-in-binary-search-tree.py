from collections import defaultdict
from typing import Optional, List

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hm = defaultdict(int)
        
        def dfs(node):
            if not node:
                return
            hm[node.val] += 1
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        max_freq = max(hm.values())
        return [key for key, value in hm.items() if value == max_freq]