# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import namedtuple, deque, defaultdict


def get_symbol(n):
    if 0 <= n < 10:
        return str(n)
    elif n == 10:
        return 'A'
    elif n == 11:
        return 'B'
    elif n == 12:
        return 'C'
    elif n == 13:
        return 'D'
    elif n == 14:
        return 'E'
    elif n == 15:
        return 'F'
    else:
        return '1' + get_symbol(n-16)  # если число больше 15, то возвращаем конкатенацию 1 и букву от разности n - 16


def get_num(sym):
    if sym == 'A':
        return 10
    elif sym == 'B':
        return 11
    elif sym == 'C':
        return 12
    elif sym == 'D':
        return 13
    elif sym == 'E':
        return 14
    elif sym == 'F':
        return 15
    else:
        return int(sym)


f_num = deque(input('Введите первое шестнадцатиричное число: ').upper())
s_num = deque(input('Введите второе шестнадцатиричное число: ').upper())

if len(f_num) < len(s_num):
    f_num, s_num = s_num, f_num

f_num.reverse()
s_num.reverse()

result = deque()
excess = 0                                 # избыток, то, что мы держим 1 в уме
i = 0
while i < len(f_num):
    sum_ = 0
    if i > len(s_num) - 1:                 # при достижении конца второго числа, дальше просто прибавляем в результат оставшиеся элементы из 1 числа
        sum_ = get_num(f_num[i]) + excess  # получаем из символа i-го элемента число и прибавляем избыток
        sum_ = get_symbol(sum_)            # полученную сумму переводим в символ

        if len(sum_) > 1:                  # если при получении символа нам вернется двойное значение (1A и тд),
            excess = 1                     # то избыток становится 1
            result.appendleft(sum_[1])     # а в результат записываем 2й элемент из полученного символа
        else:
            excess = 0                     # обнуляем избыток, т.к. ранее прибавили
            result.appendleft(sum_)        # записываем итог
        i += 1
    else:                                  # если конец второго числа не достигнут, то
        num1 = get_num(f_num[i])           # переводим i-й элемент 1 го числа в число
        num2 = get_num(s_num[i])           # переводим i-й элемент 2 го числа в число
        sum_ = num1 + num2 + excess        # прибавляем 1й, 2й элементы и избыток
        sum_ = get_symbol(sum_)            # полученную сумму переводим в символ

        if len(sum_) > 1:                  # если при получении символа нам вернется двойное значение (1A и тд),
            excess = 1                     # то избыток становится 1
            result.appendleft(sum_[1])     # а в результат записываем 2й элемент из полученного символа
        else:
            excess = 0                     # обнуляем избыток, т.к. ранее прибавили
            result.appendleft(sum_)        # прибавляем итог, прибавляем 1 к счетчику
        i += 1
else:                                      # когда i станет больше длинны 1го числа
    if excess == 1:                        # если избыток будет равен 1, то прибавляем его
        result.appendleft(str(excess))

for item in result:
    print(item, end='')