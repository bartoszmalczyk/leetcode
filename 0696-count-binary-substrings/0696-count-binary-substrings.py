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
                sol.append(temp) # number of occourences, number 
                temp = 1
                prev = curr
        sol.append(temp)
        
        ans = 0
        for i in range(len(sol) - 1):
            curr_occur = sol[i]
            nxt_occour = sol[i + 1]

            ans += min(curr_occur, nxt_occour)
        return ans
            