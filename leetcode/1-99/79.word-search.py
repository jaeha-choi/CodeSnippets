from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(ii, jj, idx):
            if ii < 0 or len(board) <= ii or jj < 0 or len(board[0]) <= jj or idx == len(word) or board[ii][jj] != word[
                idx]:
                return False
            if board[ii][jj] == word[idx] and idx == len(word) - 1:
                return True
            board[ii][jj] = "#"
            res = dfs(ii - 1, jj, idx + 1) or dfs(ii, jj - 1, idx + 1) or dfs(ii + 1, jj, idx + 1) or dfs(ii, jj + 1,
                                                                                                          idx + 1)
            board[ii][jj] = word[idx]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
