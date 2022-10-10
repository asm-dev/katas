"""
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.
"""

#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()

from functools import reduce

n = 3
student_marks = {
    "Krishna" : [67, 68, 69],
    "Arjun" : [70, 98, 63],
    "Malika" : [52, 56, 60]
}
query_name = "Malika"

marks = student_marks[query_name]
sum_marks = reduce(lambda x, y: x + y, marks, 0)
avg_marks = sum_marks/len(marks)
print("{:.2f}".format(avg_marks))