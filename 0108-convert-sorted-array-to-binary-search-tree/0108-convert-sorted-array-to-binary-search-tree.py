# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        n = len(nums)
        head_node = TreeNode(nums[n//2])
        head_node.left = self.sortedArrayToBST(nums[:(n//2)])
        head_node.right = self.sortedArrayToBST(nums[(n//2 + 1):])
        return head_node