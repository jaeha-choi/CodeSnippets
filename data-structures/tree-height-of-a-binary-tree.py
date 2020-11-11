##################################
# Problem Name: Tree: Height of a Binary Tree
# Problem URL: https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
# File generated time: 2020-11-10 23:26:00.011122
# 
# Slug: tree-height-of-a-binary-tree
# ID: 8793
# Difficulty: Easy
# Total attempts: 182823
# Successful attempts: 176691
# Success ratio: 96.65%
# Problem created at: 2015-06-17T03:49:28.000Z
# Problem updated at: 2020-09-30T08:03:54.000Z
# Deleted: False
# Can be viewed: True
##################################

# Given a binary tree, print its height.

# Enter your code here. Read input from STDIN. Print output to STDOUT

"""
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
"""


def height(root):
    lc = 0
    rc = 0

    if root.left is not None:
        lc += height(root.left) + 1
    if root.right is not None:
        rc += height(root.right) + 1

    if rc > lc:
        return rc
    else:
        return lc
