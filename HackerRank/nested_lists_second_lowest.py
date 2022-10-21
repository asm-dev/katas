# if __name__ == '__main__':
#     students_grades = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         students_grades.append([name, score])

students_grades = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2], ["Arkriti", 41], ["Harsh", 39]]

unique_scores = list(set(x[1] for x in students_grades))
ordered_scores = sorted(unique_scores)
second_lowest_score = ordered_scores[1]

second_scored = []
for student in students_grades:
    if student[1] == second_lowest_score:
        second_scored.append(student[0])

second_scored.sort()
for student in second_scored:
    print(student)