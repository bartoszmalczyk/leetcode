class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l = 0
        one_count = 0
        ans = s
        flag = False
        for r in range(len(s)):
            one_count += (s[r] == "1")
            while one_count > k: 
                one_count -= (s[l] == "1")
                l += 1
            if one_count == k:
                while s[l] != "1":
                    l += 1
                temp = s[l : r + 1]
                
                if not flag or len(temp) < len(ans):
                    ans = temp
                    flag = True
                elif len(temp) == len(ans):
                    ans = min(ans, temp)
                
        return ans if flag else ""