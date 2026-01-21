class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m = len(mat)
        diag = 0
        for i in range(m):
            diag += mat[i][i]
            diag += mat[m - i - 1][i]
        if m % 2 != 0:
            diag -= mat[m // 2][m // 2]
        return diag
            
