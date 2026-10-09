class Solution:
    def minInsertions(self, s: str) -> int:
        s = s.replace("))", "*")
        opened = 0
        ans = 0
        stack = []
        print(s)
        for i in s:
            if i == "(":
                stack.append(i)
            elif i == "*":
                if not stack:
                    ans += 1
                else:
                    stack.pop()
            if i == ")":
                if stack:
                    ans += 1
                    stack.pop()
                else:
                    ans += 2
        ans += len(stack) * 2
        return ans