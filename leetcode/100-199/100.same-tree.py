# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def solve(p, q):
            if p.val != q.val:
                return False
            res = True
            if (p.left is None) != (q.left is None):

                return False
            elif p.left and q.left:
                res = solve(p.left, q.left)

            if (p.right is None) != (q.right is None):
                return False
            elif res and p.right and q.right:
                res = solve(p.right, q.right)

            return res

        if (p is None) or (q is None):
            return (p is None) == (q is None)
        return solve(p, q)
