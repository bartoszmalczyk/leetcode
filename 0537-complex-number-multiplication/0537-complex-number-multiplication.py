class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.split("+")
        num2 = num2.split("+")
        a = int(num1[0])
        b = int(num1[1][:len(num1[1])-1])
        c = int(num2[0])
        d = int(num2[1][:len(num2[1])-1])
        ans = str(a * c - b * d) + "+" + str(a * d + b * c) + "i"
        return ans