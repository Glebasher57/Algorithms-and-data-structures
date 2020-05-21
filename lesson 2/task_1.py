# https://drive.google.com/file/d/1mOH8yUjpReQ_eHQ0xxY0ht_g0Blm9NLX/view?usp=sharing

# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
# а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0',
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

while True:
    operations = '+-*/'
    print('Введите знак операции - "+", "-", "*", "/".')
    print('Для выхода введите "0".')
    operation = input()

    if operation == '0':
        print('Bye')
        break
    elif operation not in operations:
        print('Введите верный символ операции.')
    else:
        num1 = float(input('Введите первое число: '))
        num2 = float(input('Введите второе число: '))

        if operation == '/':
            if num2 == 0:
                print('Деление на 0 невозможно, выберите верную операцию.')
                continue
            result = num1 / num2
            print(result)
        elif operation == '*':
            result = num1 * num2
            print(result)
        elif operation == '+':
            result = num1 + num2
            print(result)
        else:
            result = num1 - num2
            print(result)