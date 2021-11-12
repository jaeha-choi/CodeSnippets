from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []

        def solve(node, lvl):
            if not node:
                return

            if len(ret) - 1 < lvl:
                ret.append([])
            ret[lvl].append(node.val)

            if node.left:
                solve(node.left, lvl + 1)
            if node.right:
                solve(node.right, lvl + 1)

        solve(root, 0)
        return ret
