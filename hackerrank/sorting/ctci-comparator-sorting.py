##################################
# Problem Name: Sorting: Comparator
# Problem URL: https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem
# Time marked as solved: 2020-11-10 22:41:20.817551
# 
# Slug: ctci-comparator-sorting
# Difficulty: Medium
# Total attempts: 100049
# Successful attempts: 97325
# Success ratio: 70.00%
##################################

# Write a Comparator for sorting elements in an array.

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # def __repr__(self):

    def comparator(a, b):
        if a.score < b.score:
            return 1
        elif a.score > b.score:
            return -1
        else:
            if a.name > b.name:
                return 1
            elif a.name < b.name:
                return -1
            else:
                return 0
