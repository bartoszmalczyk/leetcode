class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = max(1, n.bit_length())
        return (~n) & ((1 << x) - 1)