# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, depth: int, node: TreeNode) -> (int, TreeNode):
        depth += 1
        depthL = depthR = depth
        currL = node.left
        currR = node.right
        if node.left:
            depthL, currL = self.helper(depth, node.left)
        if node.right:
            depthR, currR = self.helper(depth, node.right)

        if depthL == depthR:
            return depthR, node
        elif depthL > depthR:
            return depthL, currL
        else:
            return depthR, currR

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        return self.helper(-1, root)[1]
