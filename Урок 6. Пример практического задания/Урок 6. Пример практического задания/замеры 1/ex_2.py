
from functools import reduce
from memory_profiler import profile


@profile
def function_2(max_value):
    """Функция возвращает сумму квадатов четных чисел от 1 до max_value"""
    gen = (x**2 for x in range(1, max_value) if x % 2 == 0)
    value = reduce(lambda x, y: x + y, gen)
    return value


print(function_2(999999))

"""
Line #    Mem usage    Increment   Line Contents
================================================
     6     15.9 MiB     15.9 MiB   @profile
     7                             def function_2(max_value):
     8                                 '''Функция возвращает сумму квадатов четных чисел от 1 до max_value'''
     9     15.9 MiB      0.0 MiB       gen = (x**2 for x in range(1, max_value) if x % 2 == 0)
    10     15.9 MiB      0.0 MiB       value = reduce(lambda x, y: x + y, gen)
    11     15.9 MiB      0.0 MiB       return value
"""
