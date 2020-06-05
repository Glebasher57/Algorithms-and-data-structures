# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
import random, collections

m = int(input('Введите натуральное число: '))
SIZE = 2 * m + 1
array = [random.randint(0, 100) for _ in range(SIZE)]
print(array)

def comb(arr):
    gap = len(arr)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))
        swaps = False
        for i in range(len(arr) - gap):
            j = i + gap
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swaps = True

comb(array)
print(array)
median = array[len(array) // 2]
print(median)

# m = int(input('Введите натуральное число: '))
# SIZE = 2 * m + 1
# array = collections.deque(random.randint(0, 100) for _ in range(SIZE))
# arr = array.copy()
# print(array)
#
# def get_median_rec(arr): # максимум до чего смог додуматься без сортировки -_-
#     if len(arr) == 1:
#         return arr
#     min_ = arr[0]
#     max_ = arr[0]
#     for i in range(len(arr)):
#         if min_ > arr[i]:
#             min_ = arr[i]
#         elif max_ < arr[i]:
#             max_ = arr[i]
#     arr.remove(min_)
#     arr.remove(max_)
#     return get_median_rec(arr)
#
# print(get_median_rec(arr))



