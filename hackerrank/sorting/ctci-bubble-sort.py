##################################
# Problem Name: Sorting: Bubble Sort
# Problem URL: https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
# Time marked as solved: 2020-11-10 22:23:06.028037
# 
# Slug: ctci-bubble-sort
# Difficulty: Easy
# Total attempts: 160275
# Successful attempts: 156322
# Success ratio: 90.00%
##################################

# Find the minimum number of conditional checks taking place in Bubble Sort

# Complete the countSwaps function below.
def countSwaps(a):
    swaps = 0

    for i in range(len(a)):
        sort = True
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                val = a[j]
                a[j] = a[j + 1]
                a[j + 1] = val
                swaps += 1
                sort = False
        if sort:
            break
    print("Array is sorted in %d swaps." % swaps)
    print("First Element:", a[0])
    print("Last Element:", a[-1])
    return a
