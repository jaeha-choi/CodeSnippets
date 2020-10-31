##################################
# Problem Name: Counting Valleys
# Problem URL: https://www.hackerrank.com/challenges/counting-valleys/problem
# Time marked as solved: 2020-10-31 11:11:05.189138

# Slug: counting-valleys
# ID: 22936
# Difficulty: Easy
# Total attempts: 466436
# Successful attempts: 440962
# Success ratio: 94.54%
# Problem created at: 2016-07-15T13:24:38.000Z
# Problem updated at: 2020-09-23T10:33:42.000Z
# Deleted: False
# Can be viewed: True
##################################

def countingValleys(steps, path):
    # Write your code here
    level = 0
    val = 0
    flag = True
    for p in path:
        if p == "U":
            level += 1
        else:
            level -= 1

        if level < 0 and flag:
            flag = False
        elif level >= 0 and not flag:
            flag = True
            val += 1

    return val
