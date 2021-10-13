from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def mark(i, j, cnt):
            if elem == "1":
                grid[i][j] = cnt
                if i != 0 and grid[i - 1][j] == "1":
                    mark(i - 1, j, cnt)
                if j != 0 and grid[i][j - 1] == "1":
                    mark(i, j - 1, cnt)
                if i != len(grid) - 1 and grid[i + 1][j] == "1":
                    mark(i + 1, j, cnt)
                if j != len(grid[0]) - 1 and grid[i][j + 1] == "1":
                    mark(i, j + 1, cnt)

        count = 0
        for i, li in enumerate(grid):
            for j, elem in enumerate(li):
                if elem == "1":
                    count += 1
                    mark(i, j, count)
        return count
