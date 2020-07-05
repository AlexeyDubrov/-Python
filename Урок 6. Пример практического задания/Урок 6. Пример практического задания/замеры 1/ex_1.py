
from functools import reduce
from memory_profiler import profile


@profile
def function_1(max_value):
    """Функция возвращает сумму квадатов четных чисел от 0 до max_value"""
    gen = [x**2 for x in range(1, max_value) if x % 2 == 0]
    value = reduce(lambda x, y: x + y, gen)
    return value


print(function_1(999999))

"""
Результаты:
Line #    Mem usage    Increment   Line Contents
================================================
     6     15.9 MiB     15.9 MiB   @profile
     7                             def function_1(max_value):
     8                                 '''Функция возвращает сумму квадатов четных чисел от 0 до max_value'''
     9     35.1 MiB      0.3 MiB       gen = [x**2 for x in range(1, max_value) if x % 2 == 0]
    10     35.1 MiB      0.0 MiB       value = reduce(lambda x, y: x + y, gen)
    11     35.1 MiB      0.0 MiB       return value
    
Результаты на пепвый взгляд удивляют. В строке 9 существенный прирост памяти.
Но в инкременте он не отразился.
Но на деле, результаты не всегда могут быть объективными и наглядными, так отработал профилировщик

Более того, у вас вместо 35.1 может быть другое значение, на него влияют:
1) версия интерпретатора
2) версия вашей ОС и ее разрядность
3) вычислительные возможности вашей машины

И даже у меня второй вызов показал другую цифру: 35.2
Поэтому одного вызова мало. Желательно получить усредненное значение
Но об этом позже
"""
