# Решил сделать функции для генерации массивов и матриц (シ_ _)シ (многократно кланяюсь)

# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random


def get_array(size, max_item, min_item=0):
    return [random.randint(min_item, max_item) for _ in range(size)]


def get_matrix(size_a, size_b, max_item, min_item=0):
    return [[random.randint(min_item, max_item) for _ in range(size_b)] for _ in range(size_a)]


array = get_array(2, 100, -100)

print(array)

LENGTH = len(array)

min_idx = 1
min_num = array[min_idx]
max_idx = 1
max_num = array[max_idx]

i = 0
while i < LENGTH:
    if array[i] > max_num:
        max_num = array[i]
        max_idx = i
    elif array[i] < min_num:
        min_num = array[i]
        min_idx = i
    i += 1

array.insert(max_idx, min_num)
array.pop(max_idx + 1)
array.insert(min_idx, max_num)
array.pop(min_idx + 1)

print(f'{min_num} и {max_num}')
print(array)