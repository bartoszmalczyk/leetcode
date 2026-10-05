class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]
        for char in s:
            if char == "(":
                stack.append(0)
            if char == ")":
                v = stack.pop()
                w = stack.pop()
                stack.append(w + max(2 * v, 1))
        return stack.pop()

# ((() ( )(()))(()))
