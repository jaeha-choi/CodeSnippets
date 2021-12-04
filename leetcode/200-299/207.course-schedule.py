from collections import defaultdict
from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        incoming = [0 for _ in range(numCourses)]
        q = deque()

        for course, prereq in prerequisites:
            graph[course].append(prereq)
            incoming[prereq] += 1

        for i in range(len(incoming)):
            if incoming[i] == 0:
                q.append(i)

        for _ in range(numCourses):
            if len(q) == 0:
                return False
            curr = q.popleft()
            for dst in graph[curr]:
                incoming[dst] -= 1
                if incoming[dst] == 0:
                    q.append(dst)
                    incoming[curr] = -1

        return True
