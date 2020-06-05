# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
import random

SIZE = 10
array = [random.randint(-100, 100) for i in range(SIZE)]


def bubble_sort(arr, last):
    while last != 0:
        i = 0
        while i < last:
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i += 1
        last -= 1


print(array)
bubble_sort(array, len(array) - 1)
print(array) # с введением переменной ограничения стало 45 итераций в сравнении со стандартными 90


# еще что-то забавное вышло с рекурсией
# def rec_bubble_sort(arr, last):
#     if len(arr) == 1:
#         return arr.pop()
#
#     i = 0
#     while i < last:
#         if arr[i] > arr[i + 1]:
#             arr[i], arr[i + 1] = arr[i + 1], arr[i]
#         i += 1
#     return [arr.pop(), rec_bubble_sort(arr, len(arr) - 1)] # массив с массивами результатов от каждого вложения
#                                                            # как вариант для просто красивого вывода:
#                                                            # return f'{arr.pop()}, {rec_bubble_sort(arr, len(arr) - 1)}'
#                                                            # в общем чушь, еще и ограниченая глубиной :D
# print(array)
# print(rec_bubble_sort(array, len(array) - 1))