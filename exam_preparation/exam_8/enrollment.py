def gather_credits(credits_needed, *args):
    total_credits = 0
    courses = []
    for course_name, course_credits in args:
        if total_credits >= credits_needed:
            break
        if course_name in courses:
            continue
        courses.append(course_name)
        total_credits += course_credits

    if total_credits >= credits_needed:
        return f'Enrollment finished! Maximum credits: {total_credits}.\nCourses: {", ".join(sorted(courses))}'
    return f"You need to enroll in more courses! You have to gather {credits_needed - total_credits} credits more."


print(gather_credits(
    80,
    ("Basics", 27),
))
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))


