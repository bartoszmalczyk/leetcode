class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        minRows = []
        maxCol = []
        for row in matrix:
            minRows.append(min(row))

        for c in range(n):
            temp = float('-inf')
            for r in range(m):
                temp = max(matrix[r][c], temp)
            maxCol.append(temp)
        
        ans = []
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == minRows[r] and matrix[r][c] == maxCol[c]:
                    ans.append(matrix[r][c])
        return ans
