class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp = list(str(n))
        sum_ = 0
        prod = 1
        for i in temp:
            sum_ += int(i)
            prod *= int(i)
        return True if n % (sum_ + prod) == 0 else False
