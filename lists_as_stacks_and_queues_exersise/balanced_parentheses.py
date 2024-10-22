opening_parenthesis = '([{'
closing_parenthesis = ')]}'
my_stack = []
is_balanced = True

expression = input()

for character in expression:
    if character in opening_parenthesis:
        my_stack.append(character)
    elif character in closing_parenthesis:
        if not my_stack:
            is_balanced = False
            break
        last_opening_parenthesis = my_stack.pop()
        if opening_parenthesis.index(last_opening_parenthesis) != closing_parenthesis.index(character):
            is_balanced = False
            break

if is_balanced:
    print('YES')
else:
    print('NO')