import heapq
from collections import defaultdict
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        adj = defaultdict(list)
        m = len(heights)
        n = len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for r in range(m):
            for c in range(n):
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc 
                    if 0 <= nr < m and 0 <= nc < n: 
                        des = nr * n + nc
                        cost = abs(heights[nr][nc] - heights[r][c])
                        index = r * n + c
                        adj[index].append([des, cost])

        heights.clear()
        shortest = {}
        #[COST, DIS]
        minHeap = [[0,0]]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            if n1 == m * n - 1:
                return w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest: 
                    heapq.heappush(minHeap, [max(w1,w2), n2])


