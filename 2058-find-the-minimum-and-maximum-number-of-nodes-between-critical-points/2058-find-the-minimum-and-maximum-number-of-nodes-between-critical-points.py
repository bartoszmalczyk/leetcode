# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        radicals = []
        prev = None
        curr = head
        index = 0 
        while curr.next:
            if prev:
                if (
                    (prev.val < curr.val and curr.next.val < curr.val) 
                    or (prev.val > curr.val and curr.next.val > curr.val)
                ):
                    radicals.append(index)      
            index += 1
            prev = curr
            curr = curr.next
        ans = [float('inf'), -1]
        # [minDistance, maxDistance]
        if radicals: 
            ans[1] = radicals[-1] - radicals[0]
            for i in range(len(radicals) - 1):
                ans[0] = min(ans[0], radicals[i + 1] - radicals[i])
        if ans[0] == float('inf'): ans[0] = -1
        if ans[1] == 0: ans[1] = -1 
        return ans

