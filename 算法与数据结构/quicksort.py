from random import Random


def partition(arr, left, right):
    if left >= right: return left
    pv = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= pv:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


def quick_sort(arr, left, right):
    if left >= right: return arr
    p = partition(arr, left, right)
    quick_sort(arr, left, p - 1)
    quick_sort(arr, p + 1, right)
    return arr


arr = [Random().randint(1, 100) for _ in range(10)]

print(quick_sort(arr, 0, len(arr) - 1))
