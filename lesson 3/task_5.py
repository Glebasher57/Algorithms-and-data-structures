# Решл сделать  функции для генерации массивов и матриц (シ_ _)シ (многократно кланяюсь)

# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».

import random


def get_array(size, max_item, min_item=0):
    return [random.randint(min_item, max_item) for _ in range(size)]


def get_matrix(size_a, size_b, max_item, min_item=0):
    return [[random.randint(min_item, max_item) for _ in range(size_b)] for _ in range(size_a)]


array = get_array(4, 100, -100)

print(array)

LENGTH = len(array)

min_idx = 0
min_num = array[min_idx]

i = 0
while i < LENGTH:
    if 0 > array[i] > min_num:
        min_num = array[i]
        min_idx = i
    elif min_num >= 0:
        min_num = array[i]
        min_idx = i
    i += 1

if min_num >= 0:
    print('В массиве нет отрицательных чисел')
else:
    print(f'Минимальный отрицательный элемент = {min_num} под индексом {min_idx}')

