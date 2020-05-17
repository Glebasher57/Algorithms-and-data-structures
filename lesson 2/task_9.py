# https://drive.google.com/file/d/1mOH8yUjpReQ_eHQ0xxY0ht_g0Blm9NLX/view?usp=sharing

# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

summ = 0            #переменная для подсчета суммы элементов числа в цикле 'while user_num != 0'
max_sum = 0         #переменная для сохранения максимальной суммы в условии 'if summ >= max_sum'
total_num = 0       #переменная для сохранения числа с максимальной суммой элементов в условии 'if summ >= max_sum'

while True:
    user_num = input('Введите натуральное число: ')

    if user_num.isdigit() and user_num != '0':
        user_num = int(user_num)
        num = user_num     #переменная для сохранения числа пользователя, если нужно будет его заменить в total_num

        while user_num != 0:          #цикл для подсчета суммы элементов
            number = user_num % 10    #переменная для получения элемента числа
            summ += number
            user_num = user_num // 10

        if summ > max_sum:           #проверка на большую сумму элементов
            max_sum = summ
            total_num = num

        summ = 0                     #обнуление суммы

    else:
        if max_sum == 0:
            print('Первое введеное число не натуральное.')
            continue
        print(f'Наибольшая сумма элементов у числа {total_num}.')
        print(f'Сумма его элементов составила {max_sum}.')
        break