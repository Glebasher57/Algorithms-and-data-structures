# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

from lesson6_module import get_memory, get_total


sum_ = 0
max_sum = 0
total_num = 0
while True:
    user_num = input('Введите натуральное число: ')
    if user_num.isdigit() and user_num != '0':
        user_num = int(user_num)
        num = user_num

        while user_num != 0:
            number = user_num % 10
            sum_ += number
            user_num = user_num // 10

        if sum_ > max_sum:
            max_sum = sum_
            total_num = num
        sum_ = 0
    else:
        if max_sum == 0:
            print('Первое введеное число не натуральное.')
            continue
        print(f'Наибольшая сумма элементов у числа {total_num}.')
        print(f'Сумма его элементов составила {max_sum}.')
        break

print()
print(f'Итого скушанной памяти - '
      f'{get_total(get_memory(sum_), get_memory(max_sum), get_memory(total_num), get_memory(user_num), get_memory(num), get_memory(number))}')

# Вариант №1. Старый вариант
# 94 (при числах 2421, 668, 534, 31312)
# _____________________________________________________________________________________________________________________

all_nums = set()
while True:
    user_num = tuple(input('Введите натуральное число: '))
    if user_num[0].isdigit() and user_num[0] != '0':
        all_nums.add(user_num)
    else:
        if len(all_nums) == 0:
            print('Первое же введенное число не натуральное')
            continue
        break

sum_ = 0
total = 0
total_num = None
for tpl in all_nums:
    for item in tpl:
        sum_ += int(item)
    if sum_ > total:
        total = sum_
        total_num = tpl
    sum_ = 0

print(f'Наибольшая сумма элементов у числа:')
print(*total_num, sep='')
print(f'Сумма его элементов составила {total}.')

print()
print(f'Итого скушанной памяти - '
      f'{get_total(get_memory(all_nums), get_memory(user_num), get_memory(sum_), get_memory(total), get_memory(total_num))}')

# Вариант №2. Через множество кортежей
# 824 (при числах 2421, 668, 534, 31312)
# _____________________________________________________________________________________________________________________


def sum_d(num):
    if num < 10:
        return num
    return num % 10 + sum_d(num // 10)


total_num = 0
total_sum = 0
sum_ = 0
while True:
    user_num = int(input('Введите натуральное число: '))
    if user_num != 0:
        sum_ = sum_d(user_num)
        if sum_ > total_sum:
            total_sum = sum_
            total_num = user_num
    else:
        if total_num == 0:
            print('Первое же введенное число не натуральное')
            continue
        print(f'Наибольшая сумма элементов у числа {total_num}.')
        print(f'Сумма его элементов составила {total_sum}.')
        break

print()
print(f'Итого скушанной памяти - '
      f'{get_total(get_memory(total_num), get_memory(total_sum), get_memory(sum_), get_memory(user_num))}')

# Вариант №3. Уменьшил кол-во переменных в отличие от первого варианта
# 54 (при числах 2421, 668, 534, 31312)
# _____________________________________________________________________________________________________________________
