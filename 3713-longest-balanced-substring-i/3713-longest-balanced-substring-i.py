from collections import defaultdict

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0 
        
        for i in range(n):
            hm = defaultdict(int)
            max_freq = 0  
            for j in range(i, n):
                char = s[j]
                hm[char] += 1
                max_freq = max(max_freq, hm[char])
                current_len = j - i + 1
                unique_chars_count = len(hm)
                
                if max_freq * unique_chars_count == current_len:
                    ans = max(ans, current_len)
        return ans