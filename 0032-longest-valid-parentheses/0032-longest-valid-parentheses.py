
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        record = [0]

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else: #s[i] == ")"
                stack.pop()
                if not stack: 
                    stack.append(i)
                else:
                    cur = i - stack[-1]
                    record.append(cur)
        return max(record)
                 