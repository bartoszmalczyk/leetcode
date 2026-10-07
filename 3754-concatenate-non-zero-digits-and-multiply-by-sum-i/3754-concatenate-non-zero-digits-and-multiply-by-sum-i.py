class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        n_str = str(n)
        sum_ = 0
        x = ""
        for i in n_str:
            sum_ += int(i)
            if i != "0":
                x += i
        return sum_ * int(x)
        