class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(r,c): #starting at (r,c), ending at (r+2,c+2)
            temp = set()
            req = sum(grid[r][c:c+3])
            for i in range(r,r+3):
                row_sum = 0
                col_sum = 0
                for j in range(c,c+3):
                    #unique
                    if grid[i][j] in temp:
                        return False
                    else:
                        temp.add(grid[i][j])
                    #horizontal & verical 
                    row_sum += grid[i][j]
                    col_sum += grid[j][i]
                if row_sum != req or col_sum != req: return False
            #diagonal 
            first_diagonal = grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2]
            second_diagonal = grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c]
            if first_diagonal != req or second_diagonal != req: return False
            return True
        ans = 0 
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if isMagic(i,j): ans += 1
        return ans

                
