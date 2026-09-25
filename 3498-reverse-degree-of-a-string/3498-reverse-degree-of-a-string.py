class Solution:
    def reverseDegree(self, s: str) -> int:
        const = 123
        ans = 0 
        for index, char in enumerate(s):
            ans += (const - ord(char)) * (index + 1)
        return ans


