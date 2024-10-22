def calc_array_sum(arr, idx):
    if idx == len(arr) - 1:
        return arr[idx]
    return arr[idx] + calc_array_sum(arr, idx + 1)


array = list(map(int, input().split()))
result = calc_array_sum(array, 0)
print(result)

