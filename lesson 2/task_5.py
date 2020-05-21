# https://drive.google.com/file/d/1mOH8yUjpReQ_eHQ0xxY0ht_g0Blm9NLX/view?usp=sharing

# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

from math import ceil


def rec(b, e, count=10):
    if count == 0:
        return ''
    else:
        if b > e:
            return ''
        result = f'Код {b} = "{chr(b)}" | {rec(b + 1, e, count - 1)}'
        return result


begin = 32
end = 127
i = ceil((end - begin) / 10)

while i > 0:
    print(rec(begin, end))
    begin += 10
    i -= 1