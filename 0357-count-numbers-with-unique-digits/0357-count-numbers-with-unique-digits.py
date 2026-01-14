class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        const = [1, 9, 81, 648, 4536, 27216, 136080, 544320, 1632960]
        return sum(const[0:(n+1)])