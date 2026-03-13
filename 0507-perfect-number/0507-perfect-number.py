from math import ceil
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        div = []
        if num == 1:
            return False
        for i in range(2, math.ceil(num ** 0.5)):
            if num % i == 0:
                div.append(i)
                div.append(num // i)
        return sum(div) == num - 1