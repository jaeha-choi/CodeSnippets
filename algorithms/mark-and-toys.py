##################################
# Problem Name: Mark and Toys
# Problem URL: https://www.hackerrank.com/challenges/mark-and-toys/problem
# Time marked as solved: 2020-11-10 22:38:58.288152
# 
# Slug: mark-and-toys
# ID: 789
# Difficulty: Easy
# Total attempts: 155933
# Successful attempts: 145107
# Success ratio: 93.06%
# Problem created at: 2013-08-01T09:31:51.000Z
# Problem updated at: 2018-08-10T14:42:33.000Z
# Deleted: False
# Can be viewed: True
##################################

# You are Mark's best friend and have to help him buy as many toys as possible.

# Complete the maximumToys function below.
def maximumToys(prices, k):
    total = 0
    for p in sorted(prices):
        if (k - p) >= 0:
            k -= p
            total += 1
        else:
            return total
    return total

    # total = 0
    #
    # for i in range(len(prices)):
    #     for j in range(i,len(prices)):
    #         if prices[i] > prices[j]:
    #             temp = prices[i]
    #             prices[i] = prices[j]
    #             prices[j] = temp
    #
    #     if (k - prices[i]) >= 0:
    #         k -= prices[i]
    #         total += 1
    #     else:
    #         return total
    #
    # return total
