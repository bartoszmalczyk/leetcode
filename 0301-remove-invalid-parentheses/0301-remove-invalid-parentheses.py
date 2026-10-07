class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def numberToDelete(s: str) -> int:
            right = 0
            left = 0 
            for i in s:
                if i == '(':
                    left += 1
                elif i == ')':
                    if left:
                        left -= 1
                    else:
                        right += 1
            return [left, right]
        left, right = numberToDelete(s)
        ans = set()
        

        def backtracking(step, curr, left_rem, right_rem, balance):
            if balance < 0:
                return
            if step == len(s):
                if left_rem == 0 and right_rem == 0 and balance == 0:
                    ans.add(curr)
                return
            char = s[step]
            if char == '(' and left_rem > 0:
                backtracking(step + 1, curr, left_rem - 1, right_rem, balance)
            elif char == ')' and right_rem > 0:
                backtracking(step + 1, curr, left_rem, right_rem - 1, balance)
                pass

            new_balance = balance
            if char == '(':
                new_balance += 1
            elif char == ')':
                new_balance -= 1
                
            backtracking(step + 1, curr + char, left_rem, right_rem, new_balance)
        backtracking(0, "", left, right, 0)
        return list(ans)