class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        decomposition = []
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(c)
            else:
                stack.pop()
            if not stack:
                decomposition.append(i)
        prev = 0
        ans = ""
        for i in decomposition:
            print(s[prev:i + 1])
            ans += s[prev + 1:i]
            prev = i + 1
        return ans
            