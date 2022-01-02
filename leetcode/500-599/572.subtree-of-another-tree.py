# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def dfsBoth(node, sub):
            if not node or not sub or node.val != sub.val:
                return False
            res = True
            if node.left or sub.left:
                res = dfsBoth(node.left, sub.left)
            if node.right or sub.right:
                res = res and dfsBoth(node.right, sub.right)
            return res

        def dfsRoot(node):
            if node.val == subRoot.val and dfsBoth(node, subRoot):
                return True
            if (node.left and dfsRoot(node.left)) or (node.right and dfsRoot(node.right)):
                return True
            return False

        return dfsRoot(root)
