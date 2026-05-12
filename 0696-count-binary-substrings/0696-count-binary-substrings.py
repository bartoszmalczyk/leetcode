class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if not s:
            return 0 
        sol = []
        prev = s[0]
        temp = 1
        for i in range(1, len(s)):
            curr = s[i]
            if curr == prev:
                temp += 1
            else:
                sol.append([temp, prev]) # number of occourences, number 
                temp = 1
                prev = curr
        sol.append([temp, s[-1]])
        
        ans = 0
        for i in range(len(sol) - 1):
            curr_occur = sol[i][0]
            curr_nbr = sol[i][1]
            nxt_occour = sol[i + 1][0]
            nxt_nbr = sol[i + 1][1]

            if curr_nbr != nxt_nbr:
                ans += min(curr_occur, nxt_occour)
        return ans
            