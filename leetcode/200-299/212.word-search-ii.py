from typing import List


class Node:
    def __init__(self):
        self.di = {}
        self.end = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        head = Node()

        for word in words:
            curr = head
            for char in word:
                if char not in curr.di:
                    curr.di[char] = Node()
                curr = curr.di[char]
            curr.end = True

        ret = set()
        di = []

        def dfs(ii, jj, word, node):
            if ii < 0 or len(board) <= ii or jj < 0 or len(board[0]) <= jj or len(node.di) == 0 or board[ii][
                jj] not in node.di:
                return
            word += board[ii][jj]
            node = node.di[board[ii][jj]]
            tmp = board[ii][jj]
            board[ii][jj] = "#"

            if node.end and word not in ret:
                node.end = False
                ret.add(word)

            dfs(ii - 1, jj, word, node)
            dfs(ii, jj - 1, word, node)
            dfs(ii + 1, jj, word, node)
            dfs(ii, jj + 1, word, node)
            board[ii][jj] = tmp

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, "", head)
        return list(ret)
