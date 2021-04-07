##################################
# Problem Name: Hash Tables: Ransom Note
# Problem URL: https://www.hackerrank.com/challenges/ctci-ransom-note/problem
# File generated time: 2020-11-17 01:58:49.017946
# 
# Slug: ctci-ransom-note
# Difficulty: Easy
# Total attempts: 211000
# Successful attempts: 182256
# Success ratio: 90.00%
##################################

# Given two sets of dictionaries, tell if one of them is a subset of the other.
def checkMagazine(magazine, note):
    di = {}
    for elem in magazine:
        di.setdefault(elem, 0)
        di[elem] += 1

    acc = 0
    for i, elem in enumerate(note):
        if elem in di and di[elem] > 0:
            di[elem] -= 1
            acc += 1

    if len(note) == acc:
        print("Yes")
    else:
        print("No")
