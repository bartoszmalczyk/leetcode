class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        matrix = ['#' * (n - 1) for _ in range(m)]
        matrix[0] = '.' * (n - 1)
        for i in range(m):
            matrix[i] += "."
        return matrix
        
