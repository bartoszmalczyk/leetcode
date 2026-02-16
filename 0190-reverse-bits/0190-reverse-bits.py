class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        reversed_n = 0
        for i in range(32):
            reversed_n = reversed_n << 1
            bit = n & 1
            reversed_n = reversed_n | bit
            n >>= 1
        return reversed_n