##################################
# Problem Name: Sales by Match
# Problem URL: https://www.hackerrank.com/challenges/sock-merchant/problem
# Time marked as solved: 2020-10-31 11:07:48.793900

# Slug: sock-merchant
# ID: 25168
# Difficulty: Easy
# Total attempts: 623978
# Successful attempts: 571856
# Success ratio: 91.65%
# Problem created at: 2016-09-17T11:40:51.000Z
# Problem updated at: 2020-09-23T10:28:21.000Z
# Deleted: False
# Can be viewed: True
##################################

def sockMerchant(n, ar):
    di = {}
    total = 0

    for elem in ar:
        if elem in di:
            di[elem] += 1
        else:
            di[elem] = 1

    for count in di.values():
        total += count // 2

    return total
