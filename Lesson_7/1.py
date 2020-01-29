"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random
import timeit

array = [random.randint(-100, 100) for x in range(1000)]
print(array)


def bubble_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    return array


def bubble_sort_optimized(array):
    for i in range(len(array) - 1, 0, -1):
        isSorted = True  # если массив отсортирован
        for n in range(i):
            if array[n] < array[n + 1]:  # если текущий елемент меньше, чем следующий -
                array[n], array[n + 1] = array[n + 1], array[n]  # замена
                isSorted = False  # isSorted = False

        if isSorted:
            break
    return array


print(bubble_sort(array))
print(bubble_sort_optimized(array))