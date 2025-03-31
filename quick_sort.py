import random

n = 20
test_arr = random.sample(range(1, 21), n)
print(f'Unsorted array: {test_arr}')


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr.pop(random.choice(range(len(arr))))
    smaller = []
    larger = []

    for value in arr:
        if value < pivot:
            smaller.append(value)
        else:
            larger.append(value)

    return quicksort(smaller) + [pivot] + quicksort(larger)


def binary_search(arr, num, searches=0):
    searches += 1
    mid_idx = len(arr) // 2
    print(mid_idx, arr[mid_idx])

    if arr[mid_idx] == num:
        return f'Found {num} in {searches} searches!'

    if arr[mid_idx] < num:

        lower_bound = mid_idx + 1
        upper_bound = len(arr)

        return binary_search(arr[lower_bound:upper_bound], num, searches)

    if arr[mid_idx] > num:

        lower_bound = 0
        upper_bound = mid_idx
        return binary_search(arr[lower_bound:upper_bound], num, searches)


sorted_arr = quicksort(test_arr)
print(f'Sorted array: {sorted_arr}')

print(binary_search(sorted_arr, 20))

