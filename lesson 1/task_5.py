# https://drive.google.com/file/d/1yB3GEIhW7AtHySzRILR9CJCokUHpmYru/view?usp=sharing

# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

a = input('Введите первую букву: ')
b = input('Введите вторую букву: ')

num_a = ord(a) - 96
num_b = ord(b) - 96
between = num_b - num_a - 1

print(f'Буква {a} - {num_a} буква в алфавите\n'
      f'Буква {b} - {num_b} буква в алфавите\n'
      f'Букв между ними - {between}')
