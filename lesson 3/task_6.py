# Решил сделать функции для генерации массивов и матриц (シ_ _)シ (многократно кланяюсь)

# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random


def get_array(size, max_item, min_item=0):
    return [random.randint(min_item, max_item) for _ in range(size)]


def get_matrix(size_a, size_b, max_item, min_item=0):
    return [[random.randint(min_item, max_item) for _ in range(size_b)] for _ in range(size_a)]


array = get_array(20, 100, -100)

print(array)

LENGTH = len(array)
min_idx = 1
min_num = array[min_idx]
max_idx = 1
max_num = array[max_idx]
sum_ = 0

i = 0
while i < LENGTH:
    if array[i] > max_num:
        max_num = array[i]
        max_idx = i
    elif array[i] < min_num:
        min_num = array[i]
        min_idx = i
    i += 1

print(min_num, max_num)

if array[min_idx+1:max_idx]:
    for i in array[min_idx+1:max_idx]:
        sum_ += i
else:
    min_idx, max_idx = max_idx, min_idx
    for i in array[min_idx+1:max_idx]:
        sum_ += i

print(sum_)