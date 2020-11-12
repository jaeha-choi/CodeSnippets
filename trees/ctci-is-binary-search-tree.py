##################################
# Problem Name: Trees: Is This a Binary Search Tree?
# Problem URL: https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem
# File generated time: 2020-11-11 17:18:39.655142
# 
# Slug: ctci-is-binary-search-tree
# Difficulty: Medium
# Total attempts: 104667
# Successful attempts: 80105
# Success ratio: 70.00%
##################################

# Given the root of a binary tree, determine if it's a binary search tree.

# Fails 2/15 checks
# def checkBST(root):
#     flag = True
#     if root is None:
#         return flag
#
#     if root.left is not None:
#         if root.left.data >= root.data:
#             return False
#         if root.left.right is not None:
#             if root.left.right.data >= root.data:
#                 return False
#         flag = checkBST(root.left)
#     if not flag:
#         return flag
#
#     if root.right is not None:
#         if root.right.data <= root.data:
#             return False
#         if root.right.left is not None:
#             if root.right.left.data <= root.data:
#                 return False
#         flag = checkBST(root.right)
#     if not flag:
#         return flag
#     return flag

abs_mx = 10 ** 4
abs_mn = 0


def checkBSTHelper(root, mx, mn):
    lflag = True
    rflag = True

    if root.data >= mx or root.data <= mn:
        return False

    if root.left:
        lflag = checkBSTHelper(root.left, root.data, mn)

    if root.right:
        rflag = checkBSTHelper(root.right, mx, root.data)

    return lflag and rflag


def checkBST(root):
    if root is None:
        return True
    return checkBSTHelper(root, abs_mx, abs_mn)
