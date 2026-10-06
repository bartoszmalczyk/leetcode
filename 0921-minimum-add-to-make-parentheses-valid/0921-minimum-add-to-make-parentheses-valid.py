class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    ans += 1
        ans += len(stack)
        return ans
