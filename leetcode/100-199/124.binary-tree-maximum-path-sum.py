# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Uses list to store max values
    # def maxPathSum(self, root: Optional[TreeNode]) -> int:
    #     # mx = float("-inf")
    #     li = []
    #     def solve(node):
    #         if not node.left and not node.right:
    #             # mx = max(node.val, mx)
    #             li.append(node.val)
    #             return node.val
    #         l = r = float("-inf")
    #         if node.left:
    #             l = solve(node.left)
    #         if node.right:
    #             r = solve(node.right)
    #         li.append(max(l, r, l+node.val, r+node.val, l+r+node.val, node.val))
    #         return max(l+node.val, r+node.val, node.val)
    #     solve(root)
    #     return max(li)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx = float("-inf")

        def solve(node):
            nonlocal mx
            if not node.left and not node.right:
                mx = max(node.val, mx)
                return node.val
            l = r = float("-inf")
            if node.left:
                l = solve(node.left)
            if node.right:
                r = solve(node.right)
            lmax = max(l + node.val, r + node.val, node.val)
            mx = max(lmax, mx, l, r, l + r + node.val)
            return lmax

        solve(root)
        return mx
