class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = s[0]
        counter = 1
        for i in range(1,len(s)):
            if ans[-1] == s[i]:
                if counter == 1:
                    ans += s[i]
                    counter += 1
                else:
                    continue
            elif ans[-1] != s[i]:
                ans += s[i]
                counter = 1
        return ans
            

        
