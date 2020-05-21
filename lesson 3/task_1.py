# Решил сделать функции для генерации массивов и матриц (シ_ _)シ (многократно кланяюсь)

# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

import random


def get_array(size, max_item, min_item=0):
    return [random.randint(min_item, max_item) for _ in range(size)]


def get_matrix(size_a, size_b, max_item, min_item=0):
    return [[random.randint(min_item, max_item) for _ in range(size_b)] for _ in range(size_a)]


array = get_array(20, 100, 2)

print(array)

MIN_D = 2
MAX_D = 9

for i in array:
    count = 0
    for k in range(MIN_D, MAX_D + 1):
        if i % k == 0:
            count += 1
    print(f'Число {i} кратно {count} раз(а) числам в диапазоне от {MIN_D} до {MAX_D}')