"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

Пример:
Введите перове число в шестнадцатиричном формате: A2
Введите второе число в шестнадцатиричном формате: C4F
Сумма:          ['C', 'F', '1']
Произведение:   ['7', 'C', '9', 'F', 'E']
"""

from collections import namedtuple, deque


class HexCalc(object):
    def __init__(self, x):
        hl = namedtuple("HL", "A B C D E F")
        self.hex_letters = hl(A=10, B=11, C=12, D=13, E=14, F=15)
        self.x = self.to_dec(x)

    def __add__(self, other):
        return self.to_hex(self.x + other.x)

    def __mul__(self, other):
        return self.to_hex(self.x * other.x)

    def to_dec(self, x):
        dec = 0
        for i in x:
            if i in self.hex_letters._fields:
                v = self.hex_letters.__getattribute__(i)
            else:
                v = int(i)
            dec += v * (16 ** abs(len(x) - 1 - x.index(i)))
        return dec

    def to_hex(self, x):
        if x < 16:
            return [str(x)]
        else:
            r = deque()
            while x > 15:
                d = x % 16
                r.appendleft(str(d) if d < 10 else self.hex_letters._fields[d-10])
                x = x // 16
            r.appendleft(str(x) if x < 10 else self.hex_letters._fields[x-10])
            return list(r)


a = input("Введите перове число в шестнадцатиричном формате: ").upper()
b = input("Введите второе число в шестнадцатиричном формате: ").upper()

hc_a = HexCalc(a)
hc_b = HexCalc(b)

print(f"Сумма:          {hc_a + hc_b}")
print(f"Произведение:   {hc_a * hc_b}")
