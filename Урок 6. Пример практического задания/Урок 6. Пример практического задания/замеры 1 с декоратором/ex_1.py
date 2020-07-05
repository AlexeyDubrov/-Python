
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
def function_1(max_value):
    """Функция возвращает сумму квадатов четных чисел от 0 до max_value"""
    gen = [x**2 for x in range(1, max_value) if x % 2 == 0]
    value = reduce(lambda x, y: x + y, gen)
    return value


function_1(999999)

"""
m1 -  [15.66796875]
m2 -  [15.69921875]
m1 -  [15.69921875]
m2 -  [16.578125]
m1 -  [16.578125]
m2 -  [16.58984375]
m1 -  [16.58984375]
m2 -  [16.58984375]
m1 -  [16.58984375]
m2 -  [16.58984375]
0.184375 Mib
"""
