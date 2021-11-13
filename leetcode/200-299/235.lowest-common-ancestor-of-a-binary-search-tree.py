# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pv = p.val
        qv = q.val

        def solve(node):
            if node.val == pv or node.val == qv:
                return node
            if node.val <= pv and node.val <= qv:
                return solve(node.right)
            if node.val >= pv and node.val >= qv:
                return solve(node.left)
            return node

        return solve(root)
