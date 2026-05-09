class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cols= len(grid[0])
        count=0
        for row in grid:
            for j in range(cols):
                if row[j]<0:
                    count+= cols-j
                    break
        return count