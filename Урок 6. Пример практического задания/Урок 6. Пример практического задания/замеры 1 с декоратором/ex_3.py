
from functools import reduce
from pympler import tracker


def function_2(max_value):
    """Функция возвращает сумму квадатов четных чисел от 1 до max_value"""
    gen = (x**2 for x in range(1, max_value) if x % 2 == 0)
    value = reduce(lambda x, y: x + y, gen)
    return value


tr = tracker.SummaryTracker()
function_2(999999)
tr.print_diff()

"""
Допустим, мы нашли утечку, что делать дальше?
На что уходит память? Memory-profiler не показывает деталей, 
и тут на помощь нам приходит уже знакомая библиотека — pympler.

                  types |   # objects |   total size
======================= | =========== | ============
                   list |        2352 |    222.62 KB
                    str |        2349 |    161.94 KB
                    int |         421 |     11.51 KB
                   dict |           3 |    592     B
  function (store_info) |           1 |    136     B
                   cell |           2 |     96     B
                  tuple |           1 |     16     B
"""
