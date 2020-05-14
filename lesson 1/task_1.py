# https://drive.google.com/file/d/1yB3GEIhW7AtHySzRILR9CJCokUHpmYru/view?usp=sharing
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь

a = int(input('Введите трехзначное число: '))

hundreds = a // 100
tens = (a - hundreds * 100) // 10
units = a - (hundreds * 100 + tens * 10)

summ = hundreds + tens + units
mult = hundreds * tens * units

print(f'Сумма всех чисел: {summ}')
print(f'Произведение всех чисел: {mult}')
