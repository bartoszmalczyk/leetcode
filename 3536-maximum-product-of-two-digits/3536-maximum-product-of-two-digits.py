import heapq

class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []
        while n > 0:
            digits.append(-(n % 10))
            n //= 10
            
        heapq.heapify(digits)
        a = -heapq.heappop(digits)
        b = -heapq.heappop(digits)
        
        return a * b