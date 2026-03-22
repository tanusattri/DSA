class Solution:
    def reverseSubmatrix(self, grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
        top = x
        bottom = x + k - 1
        while top < bottom:
            for j in range(y, y + k):
                grid[top][j], grid[bottom][j] = grid[bottom][j], grid[top][j]
            top += 1
            bottom -= 1          
        return grid