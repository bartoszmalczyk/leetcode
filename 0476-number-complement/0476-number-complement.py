class Solution:
    def findComplement(self, num: int) -> int:
        n = num.bit_length()
        mask = int("1" * n, 2)
        return ~num & mask

"""
5 - 101
    010 
    110
"""