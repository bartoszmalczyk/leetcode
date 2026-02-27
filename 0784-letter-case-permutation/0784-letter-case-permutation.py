class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtracking(string, i):
            if len(string) == len(data): 
                ans.add(string)
                return
            if not data[i].isdigit():
                string += data[i].lower()
                backtracking(string, i + 1)
                string = string[:-1]
                string += data[i].upper()
                backtracking(string, i + 1)
            else:
                string += data[i]
                backtracking(string, i + 1)

        data = list(s)
        ans = set()
        backtracking("", 0)
        return list(ans)