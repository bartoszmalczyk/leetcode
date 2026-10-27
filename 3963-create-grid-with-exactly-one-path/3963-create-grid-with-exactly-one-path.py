class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        matrix = [['#' for _ in range(n)] for _ in range(m)]
        for i in range(n):
            matrix[0][i] = "."

        for j in range(m):
            matrix[j][-1] = "."
        ans = []
        for row in matrix:
            ans.append("".join(row))
        return ans