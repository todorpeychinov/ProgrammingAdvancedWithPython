from collections import deque

conquered_peaks = []
peaks = deque([['Vihren', 80], ['Kutelo', 90], ['Banski Suhodol', 100], ['Polezhan', 60], ['Kamenitza', 70]])
daily_portions = [int(el) for el in input().split(', ')]
daily_stamina = deque([int(el) for el in input().split(', ')])

while daily_stamina and daily_portions and peaks:
    food = daily_portions.pop()
    stamina = daily_stamina.popleft()

    result = food + stamina

    if result >= peaks[0][1]:
        conquered_peaks.append(peaks[0][0])
        peaks.popleft()
        continue

if not peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    print("\n".join(conquered_peaks))





