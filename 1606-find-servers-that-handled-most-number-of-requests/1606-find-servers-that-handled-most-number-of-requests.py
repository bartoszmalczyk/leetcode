from collections import defaultdict
from sortedcontainers import SortedSet
import heapq 

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        servers = defaultdict(int)
        avaliable = SortedSet(range(0,k))
        heap = []
        n = len(arrival) 
        for i in range(n):
            arrive = arrival[i]
            duration = load[i]
            while heap and heap[0][0] <= arrive:
                index = heapq.heappop(heap)[1]
                avaliable.add(index)
            if not avaliable: 
                continue
            idx = avaliable.bisect_left(i % k)
            if idx == len(avaliable):
                idx = 0
            chosen_server = avaliable[idx]
            avaliable.remove(chosen_server)
            heapq.heappush(heap, (arrive + duration, chosen_server))
            servers[chosen_server] += 1
            
        maximum = max(servers.values())
        ans = []
        for k,v in servers.items():
            if v == maximum:
                ans.append(k)
        return ans
