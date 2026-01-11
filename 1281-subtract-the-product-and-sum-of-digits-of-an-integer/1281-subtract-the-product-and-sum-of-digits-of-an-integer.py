class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        Sum = 0

        for i in str(n):
            x = int(i)
            product *= x
            Sum += x
        return product - Sum