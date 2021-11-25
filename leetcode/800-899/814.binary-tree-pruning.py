# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def dfs(node) -> bool:
            if not node.left and not node.right:
                return node.val == 1
            isOneL = isOneR = False
            if node.left:
                isOneL = dfs(node.left)
                if not isOneL:
                    node.left = None
            if node.right:
                isOneR = dfs(node.right)
                if not isOneR:
                    node.right = None
            return isOneL or isOneR or node.val == 1

        if not dfs(root):
            return None
        return root
