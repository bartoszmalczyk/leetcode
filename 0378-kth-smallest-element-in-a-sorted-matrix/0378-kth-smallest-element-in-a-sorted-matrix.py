class Solution:  
    def kthSmallest(self, matrix, k):
        m, n = len(matrix), len(matrix[0]) 
        maxHeap = []
        for r in range(m):
            for c in range(n):
                heappush(maxHeap, -matrix[r][c])
                if len(maxHeap) > k:
                    heappop(maxHeap)
        return -heappop(maxHeap)