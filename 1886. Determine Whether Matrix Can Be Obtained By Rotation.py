class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        res = [True, True, True, True]
        for r in range(n):
            for c in range(n):
                if mat[r][c] != target[r][c]:
                    res[0] = False
                if mat[r][c] != target[c][n - 1 - r]:
                    res[1] = False
                if mat[r][r] != target[n - 1 - r][n - 1 - c]:
                    pass 
        c0, c90, c180, c270 = True, True, True, True
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[i][j]:
                    c0 = False
                if mat[i][j] != target[j][n-1-i]:
                    c90 = False
                if mat[i][j] != target[n-1-i][n-1-j]:
                    c180 = False
                if mat[i][j] != target[n-1-j][i]:
                    c270 = False
        return c0 or c90 or c180 or c270
        
