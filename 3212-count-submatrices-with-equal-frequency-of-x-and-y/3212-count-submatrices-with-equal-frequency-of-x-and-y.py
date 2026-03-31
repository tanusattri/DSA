class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        diff_pref = [[0] * (cols + 1) for _ in range(rows + 1)]
        x_pref = [[0] * (cols + 1) for _ in range(rows + 1)]
        count = 0
        for r in range(rows):
            for c in range(cols):
                val_diff = 1 if grid[r][c] == 'X' else (-1 if grid[r][c] == 'Y' else 0)
                val_x = 1 if grid[r][c] == 'X' else 0
                diff_pref[r+1][c+1] = val_diff + diff_pref[r][c+1] + diff_pref[r+1][c] - diff_pref[r][c]
                x_pref[r+1][c+1] = val_x + x_pref[r][c+1] + x_pref[r+1][c] - x_pref[r][c]
                if diff_pref[r+1][c+1] == 0 and x_pref[r+1][c+1] > 0:
                    count += 1
        return count