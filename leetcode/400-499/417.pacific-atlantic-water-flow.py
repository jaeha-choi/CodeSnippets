from collections import defaultdict


class Solution:
    def pacificAtlantic(self, heights):
        pa = defaultdict(bool)
        at = defaultdict(bool)
        ret = []

        def dfs(ii, jj, lvl, di):
            if ii < 0 or len(heights) <= ii or jj < 0 or len(heights[0]) <= jj or di[(ii, jj)]:
                return
            if lvl > heights[ii][jj]:
                di[(ii, jj)] = False
                return
            if lvl <= heights[ii][jj]:
                di[(ii, jj)] = True
                if pa[(ii, jj)] and at[(ii, jj)]:
                    ret.append((ii, jj))
            lvl = heights[ii][jj]

            dfs(ii - 1, jj, lvl, di)
            dfs(ii, jj - 1, lvl, di)
            dfs(ii + 1, jj, lvl, di)
            dfs(ii, jj + 1, lvl, di)

        for i in range(len(heights)):
            dfs(i, 0, 0, pa)
        for j in range(len(heights[0])):
            dfs(0, j, 0, pa)

        for i in range(len(heights)):
            dfs(i, len(heights[0]) - 1, 0, at)
        for j in range(len(heights[0])):
            dfs(len(heights) - 1, j, 0, at)

        return ret
