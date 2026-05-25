class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        def is_palindrome(s):
            return s == s[::-1]
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            else:
                return is_palindrome(s[:l] + s[l + 1:]) or is_palindrome(s[:r] + s[r + 1:])
        return True  
