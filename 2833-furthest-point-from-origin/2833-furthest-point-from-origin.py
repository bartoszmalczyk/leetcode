from collections import defaultdict
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        hm = defaultdict(int)
        for i in moves:
            hm[i] += 1
        return abs(hm["L"] - hm["R"]) + hm["_"]