def softuni_students(*args, **kwargs):
    students = {}
    courses = {}
    invalid_students = []

    for course_id, username in args:
        students[username] = course_id

    for course_id, course_name in kwargs.items():
        courses[course_id] = course_name

    students_with_courses = {}

    for username, course_id in students.items():
        if course_id in courses:
            students_with_courses[username] = courses[course_id]
        else:
            invalid_students.append(username)

    invalid_students = list(sorted(invalid_students))
    sorted_students = sorted(students_with_courses.items(), key=lambda x: x[0])
    result = ''

    for username, course in sorted_students:
        result += f"*** A student with the username {username} has successfully finished the course {course}!\n"

    if invalid_students:
        result += f'!!! Invalid course students: {", ".join(invalid_students)}\n'

    return result.strip()



print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))
print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))
print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
