from collections import defaultdict

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src, dst, weight in edges:
            adj[src].append([dst, weight])
            adj[dst].append([src, 2 * weight])

        shortest = {}
        minHeap = [[0, 0]]
        while minHeap:
            n1, w1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [n2, w2 + w1])
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        return shortest[n-1]
