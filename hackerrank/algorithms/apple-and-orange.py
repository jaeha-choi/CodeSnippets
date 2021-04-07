##################################
# Problem Name: Apple and Orange
# Problem URL: https://www.hackerrank.com/challenges/apple-and-orange/problem
# Time marked as solved: 2020-10-31 11:10:10.379252

# Slug: apple-and-orange
# ID: 25220
# Difficulty: Easy
# Total attempts: 388022
# Successful attempts: 371871
# Success ratio: 95.84%
# Problem created at: 2016-09-18T16:08:36.000Z
# Problem updated at: 2020-09-23T10:27:21.000Z
# Deleted: False
# Can be viewed: True
##################################

def countApplesAndOranges(s, t, a, b, apples, oranges):
    appCnt = 0
    orgCnt = 0

    for apple in apples:
        if s <= apple + a <= t:
            appCnt += 1
    for orange in oranges:
        if s <= orange + b <= t:
            orgCnt += 1

    print(appCnt)
    print(orgCnt)
