class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans = 0
        counter = 0
        zero = False
        min_abs = abs(matrix[0][0])

        for r in matrix:
            for c in r:
                ans += abs(c)
                if c == 0: 
                    zero = True
                elif c < 0:
                    counter += 1

                min_abs = min(min_abs, abs(c))

        if zero: return ans
        if counter % 2 == 0:
            return ans
        else:
            return ans - 2*min_abs
            
