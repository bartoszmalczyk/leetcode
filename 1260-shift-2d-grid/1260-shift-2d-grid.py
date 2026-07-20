class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def shift(key, array):
            return array[-key:] + array[:-key]

        r = len(grid)
        c = len(grid[0])
        vector = [0] * r * c
        for i in range(r):
            for j in range(c):
                vector[i * c + j] = grid[i][j]
        key = k % len(vector)
        vector = shift(key, vector)
        for i in range(len(vector)):
            grid[i // c][i % c] = vector[i]
        return grid

