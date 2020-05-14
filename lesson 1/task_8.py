# https://drive.google.com/file/d/1yB3GEIhW7AtHySzRILR9CJCokUHpmYru/view?usp=sharing

# Определить, является ли год, который ввел пользователь, високосным или не високосным.

year = int(input('Введите год: '))

thousands = year // 1000
hundreds = (year - thousands * 1000) // 100
tens = (year - (hundreds * 100 + thousands * 1000)) // 10
units = year - (thousands * 1000 + hundreds * 100 + tens * 10)

if tens != 0 and units != 0:
    if year % 4 == 0:
        print(f'{year} - високосный год')
    else:
        print(f'{year} - не високосный год')
else:
    if hundreds % 4 == 0:
        print(f'{year} - високосный год')
    else:
        print(f'{year} - не високосный год')