from typing import List


class Solution:
    # def countBattleships(self, board: List[List[str]]) -> int:
    #     total = 0
    #     for i, row in enumerate(board):
    #         for j, elem in enumerate(row):
    #             if elem != ".":
    #                 total += 1
    #                 i2 = i + 1
    #                 j2 = j + 1
    #                 while i2 < len(board) and board[i2][j] != ".":
    #                     board[i2][j] = "."
    #                     i2 += 1
    #                 while j2 < len(board[0]) and board[i][j2] != ".":
    #                     board[i][j2] = "."
    #                     j2 += 1
    #     return total

    # One other answer is to detect the top-left of the battleships, which is more efficient.
    def countBattleships(self, board: List[List[str]]) -> int:
        total = 0
        for i, row in enumerate(board):
            for j, elem in enumerate(row):
                if elem != ".":
                    i2 = i - 1
                    j2 = j - 1
                    if (i == 0 or board[i2][j] == ".") and (j == 0 or board[i][j2] == "."):
                        total += 1
        return total
