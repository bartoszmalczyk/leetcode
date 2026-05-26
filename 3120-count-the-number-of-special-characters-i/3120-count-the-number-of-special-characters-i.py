class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        ans = 0
        for i in s:
            if ord(i) >= 97 and ord(i) <= 122:
                if chr(ord(i) - 32) in s:
                    ans += 1
        return ans
