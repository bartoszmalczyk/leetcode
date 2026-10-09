from functools import cache
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        @cache
        def backtracking(step, balance):
            nonlocal n
            if balance < 0:
                return False
            if step >= n:
                if balance == 0:
                    return True
                else:
                    return False

            char = s[step]
            if char == '(':
                balance += 1
                return backtracking(step + 1, balance)
            elif char == ')':
                balance -= 1
                return backtracking(step + 1, balance)
            else:
                return backtracking(step + 1, balance - 1) or backtracking(step + 1, balance + 1) or backtracking(step + 1, balance)
        return backtracking(0, 0)
            
