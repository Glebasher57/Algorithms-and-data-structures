# https://drive.google.com/file/d/18Hwc3eLoHnwHlCKaTvTiBt8YqsLo-8UZ/view?usp=sharing

# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака

a = 5
b = 6

a_and_b = a & b
a_or_b = a | b
a_expt_or_b = a ^ b
co_a = ~a
co_b = ~b
left_shift = a << 2
right_shift = a >> 2

print(f'{a} = {bin(a)} бит')
print(f'{b} = {bin(b)} бит')
print(f'{a} "И" {b} = {a_and_b} или {bin(a_and_b)} бит')
print(f'{a} "ИЛИ" {b} = {a_or_b} или {bin(a_or_b)} бит')
print(f'{a} и "Исключительное ИЛИ" {b} = {a_expt_or_b} или {bin(a_expt_or_b)} бит')
print(f'{a} и "Комплиментарный оператор" = {co_a} или {bin(co_a)} бит')
print(f'{b} и "Комплиментарный оператор" = {co_b} или {bin(co_b)} бит')
print(f'{a} и "Сдвиг влево на 2 знака" = {left_shift} или {bin(left_shift)} бит')
print(f'{a} и "Сдвиг вправо на 2 знака" = {right_shift} или {bin(right_shift)} бит')

# наверное можно было не записывать все вычисления в переменные, а выводить в принте сразу,
# но показалось, что для блок схемы так как то понятнее что ли
