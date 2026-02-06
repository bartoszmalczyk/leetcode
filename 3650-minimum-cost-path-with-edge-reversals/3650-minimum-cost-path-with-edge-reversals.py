import heapq
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
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1
            if n1 == n - 1:
                return w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w1 + w2, n2])
        return -1