##################################
# Problem Name: Birthday Cake Candles
# Problem URL: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# Time marked as solved: 2020-11-03 12:25:55.270129
# 
# Slug: birthday-cake-candles
# ID: 23074
# Difficulty: Easy
# Total attempts: 665243
# Successful attempts: 643038
# Success ratio: 96.66%
# Problem created at: 2016-07-20T09:08:23.000Z
# Problem updated at: 2020-09-23T10:40:03.000Z
# Deleted: False
# Can be viewed: True
##################################


# Determine the number of candles that are blown out.
def birthdayCakeCandles(candles):
    # Write your code here
    m = max(candles)
    cnt = 0
    for candle in candles:
        if m == candle:
            cnt += 1
    return cnt


# without using max function
def birthdayCakeCandles(candles):
    # Write your code here
    mx = 0
    cnt = 0
    for candle in candles:
        if mx < candle:
            mx = candle
            cnt = 0
        if mx == candle:
            cnt += 1
    return cnt
