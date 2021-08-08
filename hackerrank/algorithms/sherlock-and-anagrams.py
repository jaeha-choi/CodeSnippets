##################################
# Problem Name: Sherlock and Anagrams
# Problem URL: https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
# File generated time: 2021-08-07 20:51:29.504331
# 
# Slug: sherlock-and-anagrams
# ID: 5393
# Difficulty: Medium
# Total attempts: 88616
# Successful attempts: 77565
# Success ratio: 87.53%
# Problem created at: 2014-12-03T13:01:56.000Z
# Problem updated at: 2018-08-24T13:25:48.000Z
# Deleted: False
# Can be viewed: True
##################################

# Find the number of unordered anagramic pairs of substrings of a string.
#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    di = {}
    rtn = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            sort = "".join(sorted(s[i:j + 1]))
            di.setdefault(sort, 0)
            di[sort] += 1
    for value in di.values():
        rtn += (value * (value - 1)) // 2

    return rtn
