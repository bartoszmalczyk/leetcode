class Solution(object):
    def generateParenthesis(self, n):
        
        stack, ans = [], []

        def backtrack(o, close):
            if o == close == n:
                ans.append("".join(stack))
            if o < n:
                stack.append("(")
                backtrack(o+1, close)
                stack.pop()
            if o > close:
                stack.append(")")
                backtrack(o, close+1)
                stack.pop()
        backtrack(0,0)
        return ans