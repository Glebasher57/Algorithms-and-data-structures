# Решил сделать функции для генерации массивов и матриц (シ_ _)シ (многократно кланяюсь)

# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random


def get_array(size, max_item, min_item=0):
    return [random.randint(min_item, max_item) for _ in range(size)]


def get_matrix(size_a, size_b, max_item, min_item=0):
    return [[random.randint(min_item, max_item) for _ in range(size_b)] for _ in range(size_a)]


array = get_array(5, 100, -100)

print(array)

LENGTH = len(array)
f_num, f_num_idx = array[0], 0
s_num, s_num_idx = array[1], 1

if f_num > s_num:
    f_num, s_num = s_num, f_num
    f_num_idx, s_num_idx = s_num_idx, f_num_idx

i = 0
while i < LENGTH:
    k = i + 1
    while k < LENGTH:
        if array[i] >= array[k]:
            if array[k] <= f_num and k != f_num_idx:
                s_num = f_num
                f_num = array[k]
                f_num_idx = k
            elif array[k] <= s_num and k != f_num_idx:
                s_num = array[k]
        k += 1
    i += 1

print(f_num, s_num)