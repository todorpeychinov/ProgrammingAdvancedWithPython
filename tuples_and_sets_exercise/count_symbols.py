input_string = input()
characters = set(input_string)

for ch in sorted(characters):
    print(f'{ch}: {input_string.count(ch)} time/s')
