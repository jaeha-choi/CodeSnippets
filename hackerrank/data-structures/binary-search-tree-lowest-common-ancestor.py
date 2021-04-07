##################################
# Problem Name: Binary Search Tree : Lowest Common Ancestor
# Problem URL: https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem
# File generated time: 2020-11-11 00:14:17.200162
# 
# Slug: binary-search-tree-lowest-common-ancestor
# ID: 8831
# Difficulty: Easy
# Total attempts: 107304
# Successful attempts: 99800
# Success ratio: 93.01%
# Problem created at: 2015-06-19T05:27:58.000Z
# Problem updated at: 2020-09-30T08:04:40.000Z
# Deleted: False
# Can be viewed: True
##################################

# Given two nodes of a binary search tree, find the lowest common ancestor of these two nodes.

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''


def lca(root, v1, v2):
    if root.info > v1 and root.info > v2:
        return lca(root.left, v1, v2)
    elif root.info < v1 and root.info < v2:
        return lca(root.right, v1, v2)
    else:
        return root
