from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        mx = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != "0":
                    left = top = topLeft = 0
                    if 0 < j:
                        left = int(matrix[i][j - 1])
                    if 0 < i:
                        top = int(matrix[i - 1][j])
                    if 0 < i and 0 < j:
                        topLeft = int(matrix[i - 1][j - 1])

                    matrix[i][j] = min(left, top, topLeft) + 1
                    mx = max(mx, matrix[i][j])

        return mx ** 2
