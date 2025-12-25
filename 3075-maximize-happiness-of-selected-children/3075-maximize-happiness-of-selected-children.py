class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        ans = 0
        for i in range(k):
            curr = max(happiness[i] - i, 0)
            if curr <= 0:
                break
            ans += curr
        return ans
