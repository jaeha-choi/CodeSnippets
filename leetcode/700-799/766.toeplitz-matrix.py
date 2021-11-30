from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1, len(matrix)):
            j = 0
            prev = matrix[i][j]
            while j < len(matrix[i]) and i + j < len(matrix):
                if prev != matrix[i + j][j]:
                    return False
                j += 1

        for j in range(len(matrix[0])):
            i = 0
            prev = matrix[i][j]
            while i < len(matrix) and j + i < len(matrix[i]):
                if prev != matrix[i][j + i]:
                    return False
                i += 1
        return True
