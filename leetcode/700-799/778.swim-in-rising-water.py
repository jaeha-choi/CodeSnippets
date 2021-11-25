import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))
        while heap:
            val, i, j = heapq.heappop(heap)
            if j == i == len(grid) - 1:
                return val
            if 0 <= i - 1 and (i - 1, j) not in visited:
                visited.add((i - 1, j))
                heapq.heappush(heap, (max(val, grid[i - 1][j]), i - 1, j))
            if 0 <= j - 1 and (i, j - 1) not in visited:
                visited.add((i, j - 1))
                heapq.heappush(heap, (max(val, grid[i][j - 1]), i, j - 1))
            if i + 1 < len(grid) and (i + 1, j) not in visited:
                visited.add((i + 1, j))
                heapq.heappush(heap, (max(val, grid[i + 1][j]), i + 1, j))
            if j + 1 < len(grid) and (i, j + 1) not in visited:
                visited.add((i, j + 1))
                heapq.heappush(heap, (max(val, grid[i][j + 1]), i, j + 1))
