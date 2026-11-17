class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_s = ""
            for i in range(0, len(s), k):
                temp = 0
                for j in range(i, min(i + k, len(s))):
                    temp += int(s[j])
                new_s += str(temp)
            s = new_s
        return s