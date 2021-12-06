import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = [(0, k)]
        mx = -1
        visited = {}
        graph = defaultdict(list)
        for src, dst, w in times:
            graph[src].append((w, dst))

        while heap:
            w, curr = heapq.heappop(heap)
            if curr not in visited:
                for w2, dst in graph[curr]:
                    heapq.heappush(heap, (w + w2, dst))
                visited[curr] = w
                mx = max(mx, w)
        if len(visited) == n:
            return mx
        return -1
