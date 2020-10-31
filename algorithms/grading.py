##################################
# Problem Name: Grading Students
# Problem URL: https://www.hackerrank.com/challenges/grading/problem
# Time marked as solved: 2020-10-31 11:09:34.790133

# Slug: grading
# ID: 30508
# Difficulty: Easy
# Total attempts: 460752
# Successful attempts: 444856
# Success ratio: 96.55%
# Problem created at: 2017-01-06T15:46:24.000Z
# Problem updated at: 2020-09-23T10:40:04.000Z
# Deleted: False
# Can be viewed: True
##################################

def gradingStudents(grades):
    # Write your code here
    new_grade = []
    for grade in grades:
        if grade >= 38 and ((grade//5)+1)*5-grade < 3:
            new_grade.append(((grade//5)+1)*5)
        else:
            new_grade.append(grade)
    return new_grade
