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

    # second attempt
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     if not root:
    #         return []
    #     q = deque([root])
    #     res = []
    #     while q:
    #         tmp = []
    #         for _ in range(len(q)):
    #             node = q.popleft()
    #             if node.left:
    #                 q.append(node.left)
    #             if node.right:
    #                 q.append(node.right)
    #             tmp.append(node.val)
    #         res.append(tmp)
    #     return res
