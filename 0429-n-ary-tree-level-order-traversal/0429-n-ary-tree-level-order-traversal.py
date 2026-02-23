"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from collections import defaultdict
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        hm = defaultdict(list)
        def dfs(node, lvl):
            if not node: return
            hm[lvl].append(node.val)
            for children in node.children:
                dfs(children, lvl + 1)
        dfs(root,0)
        return list(hm.values())