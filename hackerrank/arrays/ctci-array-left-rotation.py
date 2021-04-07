##################################
# Problem Name: Arrays: Left Rotation
# Problem URL: https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
# File generated time: 2020-11-17 04:08:52.193697
# 
# Slug: ctci-array-left-rotation
# Difficulty: Easy
# Total attempts: 482087
# Successful attempts: 433657
# Success ratio: 90.00%
##################################

# Given an array and a number, d, perform d left rotations on the array.
def rotLeft(a, d):
    return a[d:] + a[:d]
