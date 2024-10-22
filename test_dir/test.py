import re

with open("words.txt") as file:
    words = file.read().split()

with open("input.txt") as file:
    content = file.read()

occ = {}

for word in words:
    pattern = re.compile(fr"\b{word}\b", flags=re.IGNORECASE)
    founded = re.findall(pattern, content)
    occ[word] = len(founded)

print(occ)
    