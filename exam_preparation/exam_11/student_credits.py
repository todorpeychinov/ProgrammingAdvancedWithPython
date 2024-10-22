def students_credits(*args):
    student_credits = {}
    total_credits = 0
    result = ''
    for string in args:
        course_name, current_credits, max_points, achieved_points = string.split('-')
        current_credits = int(current_credits)
        max_points = int(max_points)
        achieved_points = int(achieved_points)
        received_credits = current_credits * (achieved_points / max_points)
        student_credits[course_name] = received_credits
        total_credits += received_credits

    sorted_students_credits = sorted(student_credits.items(), key=lambda x: x[1], reverse=True)
    if total_credits >= 240:
        result += f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
    else:
        result += f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.\n"

    for course_name, credits in sorted_students_credits:
        result += f"{course_name} - {credits:.1f}\n"

    return result.strip()


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)
print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)


