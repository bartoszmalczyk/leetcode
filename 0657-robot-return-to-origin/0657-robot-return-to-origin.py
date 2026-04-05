from collections import defaultdict
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        hm = defaultdict(int)
        for direction in moves:
            hm[direction] += 1
        if hm['L'] != hm['R']:
            return False
        if hm['U'] != hm['D']:
            return False
        return True
