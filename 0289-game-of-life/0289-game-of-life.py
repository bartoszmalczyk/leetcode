class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        directions = {(0,-1), (0, 1), (-1,0), (1,0), (-1, 1), (-1,-1), (1, -1), (1,1)}
        
        def isValid(r, c):
            return 0 <= r < m and 0 <= c < n
        
        for r in range(m):
            for c in range(n):
                alive_neigh = 0
                curr_state = board[r][c] 

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc 
        
                    if isValid(nr, nc):
                        if board[nr][nc] in {1, 2}:
                            alive_neigh += 1 

                if curr_state == 1:
                    if alive_neigh < 2 or alive_neigh > 3:
                        board[r][c] = 2  
                else:
                    if alive_neigh == 3:
                        board[r][c] = 3  
                        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 2:    
                    board[r][c] = 0 
                elif board[r][c] == 3:   
                    board[r][c] = 1 