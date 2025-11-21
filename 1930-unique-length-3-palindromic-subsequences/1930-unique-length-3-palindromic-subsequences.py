class Solution:
    def countPalindromicSubsequence(self, s: str):
        unique = set(s)
        ans = 0
        for letter in unique:
            first = s.find(letter)
            last = s.rfind(letter)
            if last - first > 1:
                ans += len(set(s[first + 1 : last]))
        return ans