from collections import defaultdict

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda item: item[1])
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        
        ans = [0] * len(queries)
        used = defaultdict(int)  
        l, r = 0, 0
        m = len(logs)
        
        for query, original_idx in sorted_queries:
            ll = query - x
            rr = query
            while r < m and logs[r][1] <= rr:
                server_id = logs[r][0]
                used[server_id] += 1
                r += 1
                
            while l < m and logs[l][1] < ll:
                server_id = logs[l][0]
                used[server_id] -= 1
                if used[server_id] == 0:
                    del used[server_id]  
                l += 1
            
            ans[original_idx] = n - len(used)
            
        return ans