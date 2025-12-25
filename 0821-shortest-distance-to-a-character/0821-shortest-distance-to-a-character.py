class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = [10001] * len(s)
        zeros_position = []
        for i in range(len(s)):
            if s[i] == c:
                ans[i] = 0
                zeros_position.append(i)

        for i in range(len(ans)):
            for j in zeros_position:
                ans[i] = min(ans[i], abs(j - i))
        return ans
