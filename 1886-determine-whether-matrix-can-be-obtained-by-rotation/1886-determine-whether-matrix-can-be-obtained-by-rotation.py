class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        possible = [True, True, True, True]  
        for r in range(n):
            for c in range(n):
                if mat[r][c] != target[r][c]:
                    possible[0] = False
                if mat[r][c] != target[c][n - 1 - r]:
                    possible[1] = False
                if mat[r][c] != target[n - 1 - r][n - 1 - c]:
                    possible[2] = False
                if mat[r][c] != target[n - 1 - c][r]:
                    possible[3] = False
        return any(possible)