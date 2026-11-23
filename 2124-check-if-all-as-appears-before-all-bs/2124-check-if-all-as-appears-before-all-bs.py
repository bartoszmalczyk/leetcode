class Solution:
    def checkString(self, s: str) -> bool:
        index = 0 
        while index < len(s) and s[index] == 'a':
            index += 1

        if index >= len(s) - 1:
            return True

        while index < len(s) and s[index] == 'b':
            index += 1
        return index == len(s)
