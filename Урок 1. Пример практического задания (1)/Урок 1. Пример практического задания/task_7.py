"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""

try:
    PARAM_A = int(input('a = '))
    PARAM_B = int(input('b = '))
    PARAM_C = int(input('c = '))

    if PARAM_A + PARAM_B <= PARAM_C or PARAM_A + \
            PARAM_C <= PARAM_B or PARAM_B + PARAM_C <= PARAM_A:
        print("Треугольник не существует")
    elif PARAM_A != PARAM_B and PARAM_A != PARAM_C and PARAM_B != PARAM_C:
        print("Разносторонний")
    elif PARAM_A == PARAM_B == PARAM_C:
        print("Равносторонний")
    else:
        print("Равнобедренный")

except ValueError:
    print("Вы вместо числа ввели строку (((. Исправьтесь")
