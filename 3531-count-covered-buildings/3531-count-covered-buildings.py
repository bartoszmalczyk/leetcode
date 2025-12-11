from collections import defaultdict
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        ans = 0 
        x_hm = defaultdict(list)
        y_hm = defaultdict(list)

        for x,y in buildings:
            x_hm[x].append((x,y))
            y_hm[y].append((x,y))

        ans_potenial = set()

        for group in x_hm.values():
            if len(group) < 3: continue 
            group.sort(key=lambda p: p[1])
            
            for i in range(1, len(group) - 1):
                ans_potenial.add(group[i])
        
        for group in y_hm.values():
            if len(group) < 3: continue
            group.sort(key=lambda p: p[0])
            for i in range(1, len(group) - 1):
                if group[i] in ans_potenial:
                    ans += 1
                            
        return ans
