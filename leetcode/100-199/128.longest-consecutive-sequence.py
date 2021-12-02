from typing import List


class Node:
    def __init__(self):
        self.parent = self
        self.cnt = 1


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        graph = {}

        def find(node):
            tmp = node
            if node != node.parent:
                node = find(node.parent)
            tmp.parent = node.parent
            return node.parent

        def union(node1, node2):
            par1 = find(node1)
            par2 = find(node2)
            if par1 != par2:
                par2.parent = par1
                par1.cnt += par2.cnt
            return par1

        mx = 0
        for n in nums:
            if n not in graph:
                graph[n] = node = Node()
                if n + 1 in graph:
                    tmp = graph[n + 1]
                    node = union(node, tmp)
                mx = max(mx, node.cnt)
                if n - 1 in graph:
                    tmp = graph[n - 1]
                    tmp = union(tmp, node)
                    mx = max(mx, tmp.cnt)
        return mx
