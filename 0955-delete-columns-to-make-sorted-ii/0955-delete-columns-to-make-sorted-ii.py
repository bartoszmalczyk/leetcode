class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])
        
        ans = 0
        is_sorted = [False] * (rows - 1)

        for c in range(cols):
            must_delete = False
            for r in range(rows - 1):
                if is_sorted[r]:
                    continue
                if strs[r][c] > strs[r+1][c]:
                    must_delete = True
                    break 
            if must_delete:
                ans += 1
            else:
                for r in range(rows - 1):
                    if strs[r][c] < strs[r+1][c]:
                        is_sorted[r] = True
        return ans