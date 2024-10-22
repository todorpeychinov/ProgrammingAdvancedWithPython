def get_magic_triangle(n):
    if n == 0:
        return []

    if n == 1:
        return [[1]]

    triangle = [[1], [1, 1]]
    for i in range(2, n):
        current_row = [1]
        for j in range(1, i):
            current_row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        current_row.append(1)
        triangle.append(current_row)
    return triangle

print(get_magic_triangle(3))



