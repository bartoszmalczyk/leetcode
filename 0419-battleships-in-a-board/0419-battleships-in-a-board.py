class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        visited = set()
        m = len(board)
        n = len(board[0])
        ans = 0 
        for r in range(m):
            for c in range(n):
                if (r,c) not in visited and board[r][c] == "X": 
                    ans += 1
                    rr = r
                    while rr < m and board[rr][c] == "X":
                        rr += 1
                        visited.add((rr,c))
                    rr = r
                    while rr > 0 and board[rr][c] == "X":
                        rr -= 1
                        visited.add((rr,c))
                    cc = c
                    while cc < n and board[r][cc] == "X":
                        cc += 1
                        visited.add((r,cc))
                    cc = c
                    while cc > 0 and board[r][cc] == "X":
                        cc -= 1
                        visited.add((r,cc))
        return ans