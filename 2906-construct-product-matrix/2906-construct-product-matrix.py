class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        m = len(grid)
        n = len(grid[0])

        arr = [grid[i][j] for i in range(m) for j in range(n)]
        prefix = [1] * len(arr)
        sufix = [1] * len(arr)

        for i in range(1, len(arr)):
            prefix[i] = (prefix[i - 1] * arr[i - 1]) % 12345
        for i in range(len(arr) - 2, -1, -1):
            sufix[i] = (arr[i+1] * sufix[i + 1]) % 12345
        
        res = [(prefix[i]*sufix[i]) % 12345 for i in range(len(arr))]

        p = []
        index = 0
        
        for i in range(m):
            p.append([])
            for j in range(n):
                p[i].append(res[index])
                index += 1
        return p


     