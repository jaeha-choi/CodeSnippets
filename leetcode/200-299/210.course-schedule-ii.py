import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        q = collections.deque()
        incoming = [0 for _ in range(numCourses)]
        graph = collections.defaultdict(list)
        res = []

        for target, prereq in prerequisites:
            graph[prereq].append(target)
            incoming[target] += 1

        for i in range(numCourses):
            if incoming[i] == 0:
                q.append(i)

        for _ in range(numCourses):
            if not q:
                return []
            curr = q.popleft()
            for dst in graph[curr]:
                incoming[dst] -= 1
                if incoming[dst] == 0:
                    q.append(dst)
                    incoming[dst] = -1
            res.append(curr)
        return res
