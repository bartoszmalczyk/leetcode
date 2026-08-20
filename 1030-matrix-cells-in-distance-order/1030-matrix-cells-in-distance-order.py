class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        distances = []
        for r in range(rows):
            for c in range(cols):
                distances.append((r,c))
        def help(cell):
            return abs(cell[0] - rCenter) + abs(cell[1] - cCenter)
        return sorted(distances, key=help)
            