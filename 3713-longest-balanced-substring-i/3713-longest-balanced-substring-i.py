from collections import defaultdict

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            hm = defaultdict(int)
            max_freq = 0
            for j in range(i,n):
                c = s[j]
                hm[c] += 1
                max_freq = max(max_freq, hm[c])
                curr_len = j- i + 1
                if max_freq * len(hm) == curr_len: 
                    ans = max(ans, curr_len)
        return ans