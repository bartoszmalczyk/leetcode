import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for src, des, time in times:
            adj[src].append([des, time])
        shortest = {}
        minHeap = [[0, k]]
        while minHeap:
            n1, w1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [n2, w1 + w2])
        ans = max(shortest.values())
        if len(shortest) != n: return -1
        return ans