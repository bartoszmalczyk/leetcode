from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        res = []
        queue = deque([root])
    
        while queue:
            level_size = len(queue)
            curr_lvl = []
            for _ in range(level_size):
                node = queue.popleft()
                curr_lvl.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if len(res) % 2 == 1:
                res.append(curr_lvl[::-1])
            else:
                res.append(curr_lvl[:])
        return res