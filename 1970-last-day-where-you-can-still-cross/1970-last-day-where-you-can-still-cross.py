class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        def isPossible(day):
            grid = [[0] * col for _ in range(row)]
            for i, j in cells[:day]:
                grid[i-1][j-1] = 1

            visited = set()

            def dfs(r, c):
                if r < 0 or r >= row or c < 0 or c >= col:
                    return False
                
                if grid[r][c] == 1 or (r, c) in visited:
                    return False
                
                if r == row - 1:
                    return True

                visited.add((r, c))
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    if dfs(r + dr, c + dc):
                        return True
                return False

            for c in range(col):
                if grid[0][c] == 0: 
                    if dfs(0, c):
                        return True
            return False

        left, right = 0, len(cells)
        ans = 0        
        while left <= right:
            mid = (left + right) // 2
            if isPossible(mid):
                ans = mid      
                left = mid + 1
            else:
                right = mid - 1 
        return ans