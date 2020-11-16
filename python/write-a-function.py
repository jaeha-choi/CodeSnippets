##################################
# Problem Name: Write a function
# Problem URL: https://www.hackerrank.com/challenges/write-a-function/problem
# File generated time: 2020-11-16 13:59:03.843724
# 
# Slug: write-a-function
# ID: 22727
# Difficulty: Medium
# Total attempts: 646212
# Successful attempts: 585479
# Success ratio: 90.60%
# Problem created at: 2016-07-08T09:36:55.000Z
# Problem updated at: 2020-09-23T10:58:34.000Z
# Deleted: False
# Can be viewed: True
##################################

# Write a function to check if the given year is leap or not
def is_leap(year):
    leap = False

    # Write your logic here

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
