# https://drive.google.com/file/d/1yB3GEIhW7AtHySzRILR9CJCokUHpmYru/view?usp=sharing

# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if b < a < c:
    print(f'Среднее число {a}')
elif c < a < b:
    print(f'Среднее число {a}')
elif a < b < c:
    print(f'Среднее число {b}')
elif c < b < a:
    print(f'Среднее число {b}')
else:
    print(f'Среднее число {c}')