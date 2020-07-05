
from functools import reduce
from memory_profiler import profile


@profile
def function_3(max_value):
    """Функция возвращает сумму квадатов четных чисел от 0 до max_value"""
    gen = [x**2 for x in range(1, max_value) if x % 2 == 0]
    value = reduce(lambda x, y: x + y, gen)
    del gen
    del value
    return value


print(function_3(999999))

"""
Line #    Mem usage    Increment   Line Contents
================================================
     6     15.9 MiB     15.9 MiB   @profile
     7                             def function_3(max_value):
     8                                 '''Функция возвращает сумму квадатов четных чисел от 0 до max_value'''
     9     35.2 MiB      0.3 MiB       gen = [x**2 for x in range(1, max_value) if x % 2 == 0]
    10     35.2 MiB      0.0 MiB       value = reduce(lambda x, y: x + y, gen)
    11     16.0 MiB      0.0 MiB       del gen
    12     16.0 MiB      0.0 MiB       return value
"""
