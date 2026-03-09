
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(k):
            hours_needed = 0
            for i in piles:
                hours_needed += (i + k - 1) // k
                if hours_needed > h:
                    return False
            return True
        l = 1
        r = max(piles)
        ans = r
        while l <= r:
            mid = (l + r) // 2
            temp = canEat(mid)
            if temp:
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        return ans


