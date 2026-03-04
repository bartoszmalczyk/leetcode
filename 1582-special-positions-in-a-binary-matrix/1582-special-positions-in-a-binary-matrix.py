class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = 0
        m = len(mat)
        n = len(mat[0])
        rows = []
        cols = []
        for r in range(m):
            rows.append(sum(mat[r]))
        for c in range(n):  
            temp = 0
            for r in range(m):  
                temp += mat[r][c]  
            cols.append(temp)
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1 and rows[r] == 1 and cols[c] == 1:
                    ans += 1
        return ans