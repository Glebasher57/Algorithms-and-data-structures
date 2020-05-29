# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from collections import deque, defaultdict, namedtuple

comp_num = int(input('Сколько компаний?\n'))
comp_info = namedtuple('comp_info', 'name, quarter1, quarter2, quarter3, quarter4')

total_amount = 0
i = 1
while i <= comp_num:
    name = input(f'Введите название {i} компании: ')
    quarter1 = float(input(f'Прибыль за 1 квартал: '))
    quarter2 = float(input(f'Прибыль за 2 квартал: '))
    quarter3 = float(input(f'Прибыль за 3 квартал: '))
    quarter4 = float(input(f'Прибыль за 4 квартал: '))
    exec(f'comp_{i} = comp_info(name, quarter1, quarter2, quarter3, quarter4)')
    exec(f'total_amount += comp_{i}.quarter1 + comp_{i}.quarter2 + comp_{i}.quarter3 + comp_{i}.quarter4')
    exec(f'sum_{i} = comp_{i}.quarter1 + comp_{i}.quarter2 + comp_{i}.quarter3 + comp_{i}.quarter4')
    i += 1

avg = total_amount / comp_num
i = 1
while i <= comp_num:
    exec(f'if sum_{i} < avg: print(comp_{i}.name, "- компания с выручкой ниже среднего среди всех компаний")')
    exec(f'if sum_{i} > avg: print(comp_{i}.name, "- компания с выручкой выше среднего среди всех компаний")')
    exec(f'if sum_{i} == avg: print(comp_{i}.name, "- компания с выручкой равной средней среди всех компаний")')
    i += 1
