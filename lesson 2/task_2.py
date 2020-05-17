# https://drive.google.com/file/d/1mOH8yUjpReQ_eHQ0xxY0ht_g0Blm9NLX/view?usp=sharing

# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = input('Введите натуральное число: ')

even = 0
not_even = 0

if num.isdigit():
    for i in num:
        i = int(i)
        if i % 2 == 0:
            even += 1
        else:
            not_even += 1
    print(f'В числе {num} - {even} четных и {not_even} нечетных числа')
else:
    print('Пожалуйста, введите натуральное число')