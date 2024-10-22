from collections import deque

eggs = deque([int(el) for el in input().split(', ')])
papers = [int(el) for el in input().split(', ')]
boxes = 0

while eggs and papers:
    egg = eggs.popleft()
    paper = papers.pop()

    if egg <= 0:
        papers.append(paper)
        continue

    elif egg == 13:
        temp = papers[0]
        papers[0] = paper
        papers.append(temp)
        continue

    if (egg + paper) <= 50:
        boxes += 1
        continue

if boxes > 0:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f'Eggs left: {", ".join([str(el) for el in eggs])}')
if papers:
    print(f'Pieces of paper left: {", ".join([str(el) for el in papers])}')

