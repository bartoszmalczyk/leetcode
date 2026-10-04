class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if  -1 < i - 1 and -1 < j - 1:
                    if matrix[i][j] != matrix[i - 1][j - 1]:
                        return False
        return True

