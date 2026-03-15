class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ['a', 'b', 'c']
        counter = 1
        res = []
        def backtracking(sol):
            nonlocal counter
            if len(sol) == n:
                res.append(sol[:])
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
        print(res)
        if len(res) < k: 
            return ""
        else: 
            return "".join(res[k - 1])
"""
[['a', 'b', 'a'], 
['a', 'b', 'c'], 
['a', 'c', 'a'], 
['a', 'c', 'b'], 
['b', 'a', 'b'], 
['b', 'a', 'c'], 
['b', 'c', 'a'], 
['b', 'c', 'b'], 
['c', 'a', 'b'], 
['c', 'a', 'c'], 
['c', 'b', 'a'], 
['c', 'b', 'c']]
"""