##################################
# Problem Name: Number Line Jumps
# Problem URL: https://www.hackerrank.com/challenges/kangaroo/problem
# Time marked as solved: 2020-10-31 11:08:28.345925

# Slug: kangaroo
# ID: 22477
# Difficulty: Easy
# Total attempts: 400111
# Successful attempts: 354925
# Success ratio: 88.71%
# Problem created at: 2016-06-26T00:36:12.000Z
# Problem updated at: 2020-09-23T10:27:49.000Z
# Deleted: False
# Can be viewed: True
##################################

def kangaroo(x1, v1, x2, v2):
    curr_diff = x1 - x2
    next_diff = (x1+v1) - (x2+v2)
    if curr_diff < next_diff and curr_diff % (curr_diff-next_diff) == 0:
        return "YES"
    else:
        return "NO"
