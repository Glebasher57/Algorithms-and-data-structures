# Решил сделать функции для генерации массивов и матриц (シ_ _)シ (многократно кланяюсь)

# Определить, какое число в массиве встречается чаще всего.

import random


def get_array(size, max_item, min_item=0):
    return [random.randint(min_item, max_item) for _ in range(size)]


def get_matrix(size_a, size_b, max_item, min_item=0):
    return [[random.randint(min_item, max_item) for _ in range(size_b)] for _ in range(size_a)]


array = get_array(30, 1, -1)

print(array)

LENGTH = len(array)
LAST_INDEX = LENGTH
next_idx = 1

i = 0
count = 1
total_count = 0
item = None

while i < LENGTH:
    while array[i] in array[next_idx:LAST_INDEX]:
        if next_idx == LAST_INDEX:
            if array[i] == array[next_idx]:
                count += 1
            break
        elif array[i] != array[next_idx]:
            next_idx += 1
        else:
            next_idx += 1
            count += 1

    if count > total_count:
        total_count = count
        item = array[i]

    next_idx = 0
    count = 0
    i += 1

print(f'Число {item} встретилось в массиве {total_count} раз(а). Оно было наиболее частым.')