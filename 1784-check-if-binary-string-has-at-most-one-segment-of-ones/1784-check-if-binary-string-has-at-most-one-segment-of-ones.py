class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        temp = 0 

        for i in range(len(s) - 1):
            if s[i] == '0':
                if s[i + 1] == '1':
                    temp += 1
        return temp == 0

                    