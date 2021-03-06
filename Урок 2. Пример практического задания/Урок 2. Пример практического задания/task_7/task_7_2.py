"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""


def recur_method(numb, s=0, m=1):
    """Рекурсия"""
    if s == m:
        print(f"Равенство: {s == m}")

    elif s < m:
        return recur_method(numb, s+1, numb * (numb + 1) // 2)


try:
    NUMB = int(input("Введите число: "))
    recur_method(NUMB)
except ValueError:
    print("Вы вместо числа ввели строку (((. Исправьтесь")
