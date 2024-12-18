from decimal import Decimal, getcontext

# Установить точность до 17 знаков
getcontext().prec = 17

# global a, c
# a_glb = 3.9384077373331965
# b_glb = -3.9384077373331965
# c_glb = 7.8768051660900680

# Определи числа
c = Decimal('7.8768051660900680')
part = Decimal('1.1')
a = Decimal('3.89040561515818162')
apl = Decimal('0.99')
amn = Decimal('1.01')

# Умножение
c_new = c * part
a_start = a * apl
a_stop = a * amn

# Вывод результата
print(c_new)
# print(a_start)
# print(a)
# print(a_stop)