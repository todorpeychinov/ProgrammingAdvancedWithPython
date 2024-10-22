def bubble_sort(array):
    is_sorted = False
    i = 0
    while not is_sorted:
        is_sorted = True
        for j in range(1, len(array) - i):
            if array[j - 1] > array[j]:
                array[j], array[j - 1] = array[j - 1], array[j]
                is_sorted = False
        i += 1
    return array


numbers = [int(el) for el in input().split()]
print(*bubble_sort(numbers))