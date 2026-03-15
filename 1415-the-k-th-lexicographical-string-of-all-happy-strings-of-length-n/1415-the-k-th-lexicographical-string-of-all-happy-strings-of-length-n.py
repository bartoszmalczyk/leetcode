class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ['a', 'b', 'c']
        counter = 1
        res = []
        def backtracking(sol):
            nonlocal counter
            if len(sol) == n:
                if counter == k:
                    res.append("".join(sol[:]))
                    return True
                counter += 1
                return False

            for x in letters:
                if not sol or sol[-1] != x:
                    sol.append(x)
                    if backtracking(sol):
                        return True
                    sol.pop()
            return False
        backtracking([])
        if len(res) == 0: 
            return ""
        else: 
            return "".join(res[0])
