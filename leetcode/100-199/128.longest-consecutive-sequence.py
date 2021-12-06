from typing import List


class UFNode:
    def __init__(self):
        self.parent = self
        self.cnt = 1


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        graph = {}
        mx = 0

        def find(node):
            tmp = node
            while node is not node.parent:
                node = node.parent
            tmp.parent = node
            return node

        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)
            if parent1 is not parent2:
                parent2.parent = parent1
                parent1.cnt += parent2.cnt
            return parent1

        for elem in nums:
            if elem not in graph:
                curr = graph[elem] = UFNode()
                if elem - 1 in graph:
                    curr = union(graph[elem - 1], curr)
                if elem + 1 in graph:
                    curr = union(curr, graph[elem + 1])
                mx = max(curr.cnt, mx)
        return mx
