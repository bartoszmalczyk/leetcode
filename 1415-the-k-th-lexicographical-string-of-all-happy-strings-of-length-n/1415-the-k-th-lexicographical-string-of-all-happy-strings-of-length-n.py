class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ['a', 'b', 'c']
        counter = 1
        res = []
        def backtracking(sol):
            nonlocal counter
            if len(sol) == n:
                if counter == k:
                    res.append(sol[:])
                    return 
                counter += 1
                return
            for x in letters:
                if not sol:
                    sol.append(x)
                    backtracking(sol)
                    sol.pop()
                else:
                    if sol[-1] != x:
                        sol.append(x)
                        backtracking(sol)
                        sol.pop()
        backtracking([])
        if len(res) == 0: 
            return ""
        else: 
            return "".join(res[0])
