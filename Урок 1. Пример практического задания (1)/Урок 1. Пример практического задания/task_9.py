"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""

import sys

try:
    NUM_1 = int(input('Число 1 = '))
    NUM_2 = int(input('Число 2 = '))
    NUM_3 = int(input('Число 3 = '))

    if NUM_1 == NUM_2 == NUM_3:
        print("Введены одинаковые числа")
        sys.exit(1)

    if NUM_2 < NUM_1 < NUM_3 or NUM_3 < NUM_1 < NUM_2:
        print(f"Среднее: {NUM_1}")
    elif NUM_1 < NUM_2 < NUM_3 or NUM_3 < NUM_2 < NUM_1:
        print(f"Среднее: {NUM_2}")
    else:
        print(f"Среднее: {NUM_3}")

except ValueError:
    print("Вы вместо числа ввели строку (((. Исправьтесь")
