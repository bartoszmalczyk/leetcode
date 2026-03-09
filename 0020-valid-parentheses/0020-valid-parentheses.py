class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for par in s:
            if not stack and par in "({[":
                stack.append(par)
            elif not stack and par in ")}]":
                return False
            elif par == ")" and stack[-1] == "(":
                stack.pop()
            elif par == "]" and stack[-1] == "[":
                stack.pop()
            elif par == "}" and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(par)
        if stack:
            return False
        else: 
            return True