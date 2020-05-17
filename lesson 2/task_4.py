# https://drive.google.com/file/d/1mOH8yUjpReQ_eHQ0xxY0ht_g0Blm9NLX/view?usp=sharing

# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

print('Сколько будет элементов?')
print('(Введите натуральное число)')
amount = int(input())

count = amount
first = 1
result = 1

while count > 0:
    if first > 0:
        first /= -2
    else:
        first = abs(first)
        first /= 2
    result += first
    count -= 1

print(f'Сумма {amount} элементов = {result}')