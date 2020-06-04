# подумал, что если функции подсчета подтянуть из модуля, то наверное это тоже будет экономия памяти
# хотя может быть уже шиза наверное...

import sys


def get_memory(obj):
    total = sys.getsizeof(obj)
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'item'):
            for key, value in obj.items:
                total = total + get_memory(key) + get_memory(obj)
            return total
        elif not isinstance(obj, str):
            for item in obj:
                total += get_memory(item)
            return total
    return total


def get_total(*val):
    return sum(val)
