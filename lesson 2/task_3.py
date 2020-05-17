# https://drive.google.com/file/d/1mOH8yUjpReQ_eHQ0xxY0ht_g0Blm9NLX/view?usp=sharing

# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

# Самый приближенный к требованиям вариант, не знаю приняли бы нижние варианты или нет


def func(n, r=0):
    if n != 0:
        return func(n // 10, r * 10 + n % 10)
    else:
        return r


num = int(input('Введите натуральное число: '))

print(func(num))

# def rec(d, count=1):
#     if len(d) == count:
#         return d[0]
#     else:
#         return f'{d[len(d) - count]}{rec(d, count+1)}'
#
# num = input('Введите натуральное число: ')
#
# result = int(rec(num))
# print(result)

# Вариант с циклами

# num = input('Введите натуральное число: ')
#
# num = num[::-1]
# result = ''
# i = 0
#
# while True:
#     if num[i] != '0':
#         break
#     i += 1
#
# length = len(num) - i
#
# for j in range(0, length):
#     result += num[i]
#     i += 1
#
# print(result)
