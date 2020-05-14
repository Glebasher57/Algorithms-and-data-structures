# https://drive.google.com/file/d/1yB3GEIhW7AtHySzRILR9CJCokUHpmYru/view?usp=sharing

# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if a > b and a < c:
    print(f'Среднее число {a}')
elif a > c and a < b:
    print(f'Среднее число {a}')
elif b > a and b < c:
    print(f'Среднее число {b}')
elif b > c and b < a:
    print(f'Среднее число {b}')
else:
    print(f'Среднее число {c}')