# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

matrix = []

for i in range(5):
    arr = []
    for j in range(3):
        print(f'{j+1} элемент {i+1} линии.')
        item = float(input('Введите целое число: '))
        arr.append(item)
    matrix.append(arr)

i = 0
for line in matrix:
    sum_items = 0
    for j, item in enumerate(line):
        sum_items += item
    matrix[i].append(sum_items)
    i += 1

for line in matrix:
    for item in line:
        print(f'{item:>10}', end='')
    print('\n')