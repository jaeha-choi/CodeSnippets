# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def maxDepth(self, root: TreeNode, size) -> int:
    #     mx = 0
    #     if
    # def maxDepth(self, root: TreeNode) -> int:
    #     if root is None:
    #         return 0
    #     left = 0
    #     if root.left is not None:
    #         left += self.maxDepth(root.left)
    #     right = 0
    #     if root.right is not None:
    #         right += self.maxDepth(root.right)
    #     return max(left, right) + 1

    # second attempt
    def maxDepth(self, root: TreeNode) -> int:
        def solve(node):
            l = r = 1
            if not node:
                return 0
            if node.left:
                l += solve(node.left)
            if node.right:
                r += solve(node.right)
            return max(l, r)

        return solve(root)
