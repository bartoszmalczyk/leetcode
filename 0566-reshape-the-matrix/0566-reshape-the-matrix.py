class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if r * c != m * n:
            return mat
        else:
            counter = 0
            ans = []
            for i in range(r):
                ans.append([])
                for _ in range(c):
                    ans[i].append(mat[counter // n][counter % n])
                    counter += 1
            return ans 
