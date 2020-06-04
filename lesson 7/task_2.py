# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random

SIZE = 10
array = [round(random.uniform(0, 50), 2) for i in range(SIZE)]


def merging(left_arr, right_arr):
    merge = []
    start_left = start_right = 0
    left_len, right_len = len(left_arr), len(right_arr)
    for _ in range(left_len + right_len):
        if start_right < right_len and start_left < left_len:
            if left_arr[start_left] <= right_arr[start_right]:
                merge.append(left_arr[start_left])
                start_left += 1
            else:
                merge.append((right_arr[start_right]))
                start_right += 1
        elif start_left == left_len:
            merge.append(right_arr[start_right])
            start_right += 1
        elif start_right == right_len:
            merge.append(left_arr[start_left])
            start_left += 1
    return merge


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merging(left, right)


print(array)
print(merge_sort(array))