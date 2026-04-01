class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        MOD = 12345
        p = [[1] * m for _ in range(n)]
        cumulative_prod = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = cumulative_prod
                cumulative_prod = (cumulative_prod * grid[i][j]) % MOD
        cumulative_prod = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                p[i][j] = (p[i][j] * cumulative_prod) % MOD
                cumulative_prod = (cumulative_prod * grid[i][j]) % MOD
        return p