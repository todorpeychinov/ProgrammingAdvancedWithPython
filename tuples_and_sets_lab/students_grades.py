number_of_students = int(input())
students = {}

for _ in range(number_of_students):
    data = tuple(input().split())
    name, grade = data
    grade = float(grade)

    if name not in students:
        students[name] = []

    students[name].append(grade)

for student, grades in students.items():
    print(f'{student} -> {" ".join([f"{current_grade:.2f}" for current_grade in grades])} (avg: {(sum(grades) / len(grades)):.2f})')


