# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.

import timeit
import cProfile


def test_func(func):
    arr = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
        37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
        79, 83, 89, 97, 101, 103, 107, 109, 113,
        127, 131, 137, 139, 149, 151, 157, 163,
        167, 173, 179, 181, 191, 193, 197, 199
    ]

    for i, item in enumerate(arr):
        assert item == func(i+1, 200)
        print(f'Test {i+1} OK')


def sieve(num, rng):
    sieve = [i for i in range(rng)]
    sieve[1] = 0

    for i in range(2, rng):
        if sieve[i] != 0:
            j = i + i
            while j < rng:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]

    return res[num-1]


print('Тест sieve\n')
test_func(sieve)
print()
print(timeit.timeit('sieve(10, 30)', number=1000, globals=globals()))      # 0.013153400000000003
print(timeit.timeit('sieve(100, 542)', number=1000, globals=globals()))    # 0.36200550000000004
print(timeit.timeit('sieve(1000, 7920)', number=1000, globals=globals()))  # 4.799201099999999

cProfile.run('sieve(10, 30)')      # 1    0.000    0.000    0.000    0.000 task_2.py:23(sieve)
cProfile.run('sieve(100, 542)')    # 1    0.000    0.000    0.000    0.000 task_2.py:23(sieve)
cProfile.run('sieve(1000, 7920)')  # 1    0.004    0.004    0.004    0.004 task_2.py:23(sieve)

# В данном случае и по третий вариант, как я понял, N является размером решета
# Поэтому подгонял размер, до необходимых для поиска чисел
# Вариант №1 похож на квадратный


def prime_number(num, rng):
    arr = [i for i in range(2, rng) if i % 2 != 0]
    total = [2]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] % arr[j] == 0:
                if i == j:
                    total.append(arr[i])
                    break
                break
            elif j == len(arr)+1:
                total.append(arr[i])
    return total[num-1]


print('-' * 50)
print('Тест prime_number\n')
test_func(prime_number)
print()
print(timeit.timeit('prime_number(10, 30)', number=100, globals=globals()))      # 0.0030029000000002526
print(timeit.timeit('prime_number(100, 542)', number=100, globals=globals()))    # 0.4520375000000003
print(timeit.timeit('prime_number(1000, 7920)', number=100, globals=globals()))  # 81.3340047

cProfile.run('prime_number(10, 30)')      # 1    0.000    0.000    0.000    0.000 task_2.py:55(prime_number)
cProfile.run('prime_number(100, 542)')    # 1    0.006    0.006    0.007    0.007 task_2.py:55(prime_number)
cProfile.run('prime_number(1000, 7920)')  # 1    0.999    0.999    1.278    1.278 task_2.py:55(prime_number)

# Вариант №2 похож на кубический


# import sys
# sys.setrecursionlimit(1500) #стандартной глубины не хватает

def sieve_rec(num, rng):
    dict_ = {1: 2, 2: 3}

    def _sieve_rec(num):
        if num in dict_:
            return dict_[num]
        else:
            prev = _sieve_rec(num - 1)
            last_ord_number = len(dict_)
            while last_ord_number != num:
                prev += 1
                if prev % 2 == 0:
                    continue

                count = 3
                while prev % count != 0:
                    count += 2

                if prev == count:
                    last_ord_number += 1
                    dict_[last_ord_number] = prev
                    return dict_[last_ord_number]

    return _sieve_rec(num)


print('-' * 50)
print('Тест sieve_rec\n')
test_func(sieve_rec)
print()
print(timeit.timeit('sieve_rec(10)', number=1000, globals=globals()))    # 0.013543700000000006
print(timeit.timeit('sieve_rec(100)', number=1000, globals=globals()))   # 1.3335721
print(timeit.timeit('sieve_rec(1000)', number=1000, globals=globals()))  # 245.91391420000002

cProfile.run('sieve_rec(10)')    # 9/1    0.000    0.000    0.000    0.000 scratch_1.py:20(sieve_rec)
cProfile.run('sieve_rec(100)')   # 99/1    0.001    0.000    0.001    0.001 scratch_1.py:20(sieve_rec)
cProfile.run('sieve_rec(1000)')  # 999/1    0.269    0.000    0.269    0.269 scratch_1.py:20(sieve_rec)

# Вариант №3 не знаю на что похож


def get_prime_num(num, rng):
    ord_number = 1
    digit = 2
    while ord_number != num:
        digit += 1
        count = 3

        if digit % 2 == 0:
            continue

        while digit % count != 0:
            count += 2
        if count == digit:
            ord_number += 1
    else:
        return digit


print('-' * 50)
print('Тест get_prime_num\n')
test_func(get_prime_num)
print()
print(timeit.timeit('get_prime_num(10)', number=1000, globals=globals()))    # 0.01153199999998833
print(timeit.timeit('get_prime_num(100)', number=1000, globals=globals()))   # 1.3918180000000575
print(timeit.timeit('get_prime_num(1000)', number=1000, globals=globals()))  # 248.33675069999993

cProfile.run('get_prime_num(10)')    # 1    0.000    0.000    0.000    0.000 task_2.py:115(get_prime_num)
cProfile.run('get_prime_num(100)')   # 1    0.002    0.002    0.002    0.002 task_2.py:115(get_prime_num)
cProfile.run('get_prime_num(1000)')  # 1    0.231    0.231    0.231    0.231 task_2.py:115(get_prime_num)

# Вариант №4 похож на линейный, наверное
