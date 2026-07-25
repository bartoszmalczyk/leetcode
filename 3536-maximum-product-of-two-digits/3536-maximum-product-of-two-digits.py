import heapq
class Solution:
    def maxProduct(self, n: int) -> int:
        max_heap = []
        while n >= 1:
            heapq.heappush(max_heap, -1 * (n % 10))
            n //= 10
        a = heappop(max_heap) * -1
        b = heappop(max_heap) * -1
        return a * b