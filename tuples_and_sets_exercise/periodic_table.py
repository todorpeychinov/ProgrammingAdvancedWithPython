unique_elements = set()

for _ in range(int(input())):
    elements = input().split()

    for el in elements:
        unique_elements.add(el)

print(*unique_elements, sep='\n')