class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        ans = 0
        for i in s:
            if i == ")":
                stack.pop()
            elif i == "(":
                stack.append("(")
                ans = max(ans, len(stack))
        return ans
