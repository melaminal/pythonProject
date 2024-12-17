from decimal import Decimal, getcontext

# Установить точность до 17 знаков
getcontext().prec = 17

# global a, c
# a_glb = 3.9384077373331965
# b_glb = -3.9384077373331965
# c_glb = 7.8768051660900680

# Определи числа
c = Decimal('7.8768051660900680')

# Умножение
c_new = c * 1.0025

# Вывод результата
print(c_new)