"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""

import copy
import timeit
from random import randint
from statistics import median


def mid_num_1(list_for_sorting):
    temp = list_for_sorting
    left_list = []
    right_list = []
    for i in range(len(temp)):
        for j in range(len(temp)):
            if temp[i] > temp[j]:
                left_list.append(temp[j])
            if temp[i] < temp[j]:
                right_list.append(temp[j])
            if temp[i] == temp[j] and i > j:
                left_list.append(temp[j])
            if temp[i] == temp[j] and i < j:
                right_list.append(temp[j])
        if len(left_list) == len(right_list):
            return temp[i]
        left_list.clear()
        right_list.clear()


def mid_num_2(list_for_sorting):
    """
    Возвращает медиану массива путем удаления максимальных элементов,
    пока максимальным не будет медиана.
    """
    temp_list = list_for_sorting
    for i in range(len(list_for_sorting) // 2):
        temp_list.remove(max(temp_list))
    return max(temp_list)


def gnome_sort(sort_list):
    """
    Сортировка списка методом gnome_sort
    """
    i = 1
    while i < len(sort_list):
        if not i or sort_list[i - 1] <= sort_list[i]:
            i += 1
        else:
            sort_list[i], sort_list[i - 1] = sort_list[i - 1], sort_list[i]
            i -= 1
    return sort_list


def gnome_median(sort_list):
    return gnome_sort(sort_list)[len(sort_list) // 2]


UNSORTED_LIST = [randint(0, 100) for i in range(2 * randint(10, 100) + 1)]
TO_SORT = copy.copy(UNSORTED_LIST)

print(f'UNSORTED_LIST:\n{UNSORTED_LIST}\n')
# Нахождение медианы через встроенную функцию
print(f'Медиана - {median(UNSORTED_LIST)}')
# Нахождение медианы через удаление максимальных элементов
print(f'Медиана (mid_num_1) - {mid_num_1(UNSORTED_LIST)}')
# Нахождение медианы без сортировки исходного массива
print(f'Медиана (left/right lists) - {mid_num_2(UNSORTED_LIST)}')
# сортированный список
print(f'Медиана (sort list) - {gnome_median(TO_SORT)}\n')

print(f'test_1 (median) {timeit.timeit("median(UNSORTED_LIST)", globals=globals(), number=100)} milliseconds')
print(f'test_2 (mid_num_1) {timeit.timeit("mid_num_1(UNSORTED_LIST)", globals=globals(), number=100)} milliseconds')
print(f'test_3 (left/right lists) {timeit.timeit("mid_num_1(UNSORTED_LIST)", globals=globals(), number=100)} milliseconds')
print(f'test_3 (lsort list) {timeit.timeit("gnome_median(TO_SORT)", globals=globals(), number=100)} milliseconds')
