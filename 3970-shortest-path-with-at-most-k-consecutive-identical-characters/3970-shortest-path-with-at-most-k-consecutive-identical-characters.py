from collections import defaultdict
import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        paths = defaultdict(list)
        for s, e, w in edges:
            paths[s].append((e, w))
        pq = [(0, 0, 1)]
        dist = {}
        dist[(0, 1)] = 0
        
        while pq:
            d, u, count = heapq.heappop(pq)
            if u == n - 1:
                return d

            if d > dist.get((u, count), float('inf')):
                continue 
                
            for v, w in paths[u]:
                if labels[u] == labels[v]:
                    next_count = count + 1
                else:
                    next_count = 1

                if next_count > k:
                    continue
                
                next_d = d + w
                
                if next_d < dist.get((v, next_count), float('inf')):
                    dist[(v, next_count)] = next_d
                    heapq.heappush(pq, (next_d, v, next_count))
        return -1