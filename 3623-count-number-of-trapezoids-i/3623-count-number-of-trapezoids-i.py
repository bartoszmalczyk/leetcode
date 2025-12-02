import math
from collections import defaultdict
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        coordinates = defaultdict(int)
        ans = 0
        for x,y in points:
            coordinates[y] += 1
        
        combinations = []
        posibilites = list(coordinates.values())
        for i in posibilites:
            combinations.append(math.comb(i, 2))

        total_sum = sum(combinations)
        sum_sq = sum(c * c for c in combinations)
        ans = (total_sum * total_sum - sum_sq) // 2
        
        return ans % (10**9 + 7)
"""
jest wzorek ze jak jest [1,2,3,4] i chce się zrobić: 1*2 + 1*3 + 1*4 + 2*3 + 2*4 + 3*4 to mozna po prostu:
[ (suma)^2 + (Σ elementow^2) ] / 2
"""
                
