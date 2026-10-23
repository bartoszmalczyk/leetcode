class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        y = len(grid)
        x = len(grid[0])
        res = 0

        for j in range(0, y):
            for i in range(0, x):
                if grid[j][i] == 1:
                    res += 4

                    if i < x - 1 and grid[j][i + 1] == 1:
                        res -= 2
                    if j < y - 1 and grid[j + 1][i] == 1:
                        res -= 2

        return res


                    