# Проанализировать скорость и сложность одного любого алгоритма
# из разработанных в рамках домашнего задания первых трех уроков.

# Выбрал задание из занятия 3 упражнение 4.
# Определить, какое число в массиве встречается чаще всего.

import timeit, cProfile, random

def get_array(size, max_item, min_item=0):
    return [random.randint(min_item, max_item) for _ in range(size)]

def oftened_digit1(n):
    array = get_array(n, 1, -1)

    LENGTH = len(array)
    LAST_INDEX = LENGTH
    next_idx = 1

    i = 0
    count = 1
    total_count = 0

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

        next_idx = 0
        count = 0
        i += 1

    return total_count


# print(timeit.timeit('oftened_digit1(10)', number=100, globals=globals()))       # 0.012933099999999996
# print(timeit.timeit('oftened_digit1(100)', number=100, globals=globals()))      # 0.6612596
# print(timeit.timeit('oftened_digit1(1000)', number=100, globals=globals()))     # 141.84048130000002
#
# cProfile.run('oftened_digit1(10)')       # 1    0.000    0.000    0.000    0.000 scratch.py:12(oftened_digit1)
# cProfile.run('oftened_digit1(100)')      # 1    0.007    0.007    0.007    0.007 scratch.py:12(oftened_digit1)
# cProfile.run('oftened_digit1(1000)')     # 1    1.490    1.490    1.493    1.493 scratch.py:12(oftened_digit1)

# Вариант №1 похож на самый ужасный и действительно им является.
# Думаю у него квадратная асимптотика или как это говорится...


def oftened_digit2(n):
    array = get_array(n, 1, -1)

    total_count = 1
    for i in range(len(array)):
        count = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                count += 1
        if count > total_count:
            total_count = count
    return total_count


# print(timeit.timeit('oftened_digit2(10)', number=100, globals=globals()))       # 0.005347199999999996
# print(timeit.timeit('oftened_digit2(100)', number=100, globals=globals()))      # 0.10527250000000002
# print(timeit.timeit('oftened_digit2(1000)', number=100, globals=globals()))     # 8.7019929
#
# cProfile.run('oftened_digit2(10)')       # 1    0.000    0.000    0.000    0.000 scratch.py:53(oftened_digit2)
# cProfile.run('oftened_digit2(100)')      # 1    0.001    0.001    0.001    0.001 scratch.py:53(oftened_digit2)
# cProfile.run('oftened_digit2(1000)')     # 1    0.103    0.103    0.105    0.105 scratch.py:53(oftened_digit2)

# Вариант №2 похож на квадратный

def oftened_digit3(n):
    array = get_array(n, 1, -1)
    counter = {}
    count = 1
    for item in array:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1

        if counter[item] > count:
            count = counter[item]
    return count

print(timeit.timeit('oftened_digit3(10)', number=100, globals=globals()))       # 0.001558900000000002
print(timeit.timeit('oftened_digit3(100)', number=100, globals=globals()))      # 0.0120841
print(timeit.timeit('oftened_digit3(1000)', number=100, globals=globals()))     # 0.1381807

cProfile.run('oftened_digit3(10)')       # 1    0.000    0.000    0.000    0.000 scratch.py:81(oftened_digit3)
cProfile.run('oftened_digit3(100)')      # 1    0.000    0.000    0.000    0.000 scratch.py:81(oftened_digit3)
cProfile.run('oftened_digit3(1000)')     # 1    0.000    0.000    0.004    0.004 scratch.py:81(oftened_digit3)

# Вариант №3, через счетчик-множество оказался самым быстрым вариантом. Похож на линейный.