from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q = deque()
        graph = {}
        incoming = [0] * numCourses
        res = deque()
        # res = []

        for i in range(numCourses):
            graph.setdefault(i, [])

        for src, dst in prerequisites:
            graph[src].append(dst)
            incoming[dst] += 1

        for i in range(len(incoming)):
            if incoming[i] == 0:
                q.append(i)
                incoming[i] = -1

        for _ in range(len(graph)):
            if not q:
                return []
            src = q.popleft()
            for dst in graph[src]:
                incoming[dst] -= 1
                if incoming[dst] == 0:
                    q.append(dst)
                    incoming[dst] = -1
            # res.append(src)
            res.appendleft(src)

        # return res[::-1]
        return res
