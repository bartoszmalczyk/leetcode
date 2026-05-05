class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        temp = ""
        s = s.lower()

        for c in s:
            if c.isalpha() or c.isnumeric():
                temp += c

        return temp == temp[::-1]