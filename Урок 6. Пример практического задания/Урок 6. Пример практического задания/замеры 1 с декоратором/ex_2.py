
from functools import reduce
from memory_profiler import profile, memory_usage


def memory_checker(func):
    def start(*args, **kwargs):

        mem_diff = []
        for i in range(5):

            m1 = memory_usage()
            print(f'm1 - {m1}')

            func(args[0])


            m2 = memory_usage()

            print(f'm2 - {m2}')

            mem_diff.append(m2[0] - m1[0])

        print(f'{sum(mem_diff)/5} Mib')
    return start


@memory_checker
def function_2(max_value):
    """Функция возвращает сумму квадатов четных чисел от 1 до max_value"""
    gen = (x**2 for x in range(1, max_value) if x % 2 == 0)
    value = reduce(lambda x, y: x + y, gen)
    return value


function_2(999999)

"""
m1 - [15.671875]
m2 - [15.69140625]
m1 - [15.69140625]
m2 - [15.69140625]
m1 - [15.69140625]
m2 - [15.69140625]
m1 - [15.69140625]
m2 - [15.69140625]
m1 - [15.69140625]
m2 - [15.69140625]
0.00390625 Mib
"""
