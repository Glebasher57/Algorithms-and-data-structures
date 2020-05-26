# Решил сделать функции для генерации массивов и матриц (シ_ _)シ (многократно кланяюсь)

# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random


def get_array(size, max_item, min_item=0):
    return [random.randint(min_item, max_item) for _ in range(size)]


def get_matrix(size_a, size_b, max_item, min_item=0):
    return [[random.randint(min_item, max_item) for _ in range(size_b)] for _ in range(size_a)]


array = get_array(20, 100, -100)

print(array)

length = len(array)
arr2 = []

i = 0

while i < length:
    if array[i] % 2 == 0:
        arr2.append(array[i])
    i += 1

print(arr2)

#for i in array:
#    if i % 2 == 0:
#        arr2.append(i)
#
#print(arr2)