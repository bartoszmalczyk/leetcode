# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.array = []
        self.curr = 0
    
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.array.append(node.val) 
            dfs(node.right)
            
        dfs(root)

    def next(self) -> int:
        val = self.array[self.curr]
        self.curr += 1  
        return val

    def hasNext(self) -> bool:
        return self.curr < len(self.array)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()