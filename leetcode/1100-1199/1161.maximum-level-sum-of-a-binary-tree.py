# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        di = {}

        def helper(node, level):
            di.setdefault(level, 0)
            di[level] += node.val
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 1)
        return max(di, key=di.get)
