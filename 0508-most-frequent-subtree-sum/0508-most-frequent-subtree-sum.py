# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict 
from functools import cache
class Solution:

    def findFrequentTreeSum(self, root: TreeNode | None) -> list[int]:
        ans = []
        @cache
        def solution(node):
            if not node:
                return 0 
            x = node.val + solution(node.left) + solution(node.right)
            ans.append(x)
            return x
        solution(root)
        x = Counter(ans)
        most_frequent = max(set(ans), key=ans.count)
        sol = []
        for v, _ in x.items():
            if x[v] == x[most_frequent]:
                sol.append(v)
        return sol

