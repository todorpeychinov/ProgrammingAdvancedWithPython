from collections import deque

vowels = deque(input().split())
consonants = input().split()

searched_words = ["rose", "tulip", "lotus", "daffodil"]
word_founded = False
founded_letters = []

while vowels and consonants and not word_founded:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for word in searched_words:
        if vowel in word:
            founded_letters.append(vowel)
        if consonant in word:
            founded_letters.append(consonant)

        if all([c in founded_letters for c in word]):
            print(f"Word found: {word}")
            word_founded = True
            break

if not word_founded:
    print("Cannot find any word!")

if vowels:
    print(f'Vowels left: {" ".join(str(el) for el in vowels)}')
if consonants:
    print(f'Consonants left: {" ".join(str(el) for el in consonants)}')







