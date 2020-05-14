# https://drive.google.com/file/d/1yB3GEIhW7AtHySzRILR9CJCokUHpmYru/view?usp=sharing

# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

a = int(input('Введите номер буквы: '))
a = chr(a + 96)

print(f'Это буква {a}')