class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        CONST = 97
        p_letters = [0] * 26
        s_letters = [0] * 26 
        ans = [] 
        n_s = len(s)
        n_p = len(p)

        if n_p > n_s:
            return ans
        
        for char in p:
            p_letters[ord(char) - CONST] += 1

        for i in range(n_p):
            s_letters[ord(s[i]) - CONST] += 1
        if s_letters == p_letters: ans.append(0)

        for i in range(n_s - n_p):
            s_letters[ord(s[i]) - CONST] -= 1
            s_letters[ord(s[i + n_p]) - CONST] += 1
            if s_letters == p_letters: ans.append(i + 1)
        return ans
        
