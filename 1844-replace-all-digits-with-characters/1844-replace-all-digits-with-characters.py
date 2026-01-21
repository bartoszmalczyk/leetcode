class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(x,n):
            return chr((ord(x) + int(n)))
        s = list(s)
        for i in range(0, len(s) - 1, 2):
            s[i + 1] = shift(s[i], s[i + 1])
        return "".join(s)