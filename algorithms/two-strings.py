##################################
# Problem Name: Two Strings
# Problem URL: https://www.hackerrank.com/challenges/two-strings/problem
# File generated time: 2020-11-17 02:01:26.069566
# 
# Slug: two-strings
# ID: 5187
# Difficulty: Easy
# Total attempts: 223763
# Successful attempts: 199804
# Success ratio: 89.29%
# Problem created at: 2014-11-14T21:20:01.000Z
# Problem updated at: 2018-07-10T15:57:01.000Z
# Deleted: False
# Can be viewed: True
##################################

# Given two strings, you find a common substring of non-zero length.
def twoStrings(s1, s2):
    d1 = set([ch for ch in s1])
    d2 = set([ch for ch in s2])

    for elem in d1:
        if elem in d2:
            return "YES"
    return "NO"
