from collections import deque 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = deque()
        letters = set()
        sol = 0
        for char in s:
            while char in letters:
                letters.remove(ans.popleft())
            letters.add(char)
            ans.append(char)
            
            sol = max(sol, len(ans))
        return sol