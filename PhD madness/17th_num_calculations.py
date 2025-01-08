from decimal import Decimal, getcontext

from mpmath import sqrtm

# Установить точность до 17 знаков
getcontext().prec = 17

# global a, c
# a_glb =
# b_glb =
# c_glb =

# Определи числа
a = Decimal('3.8894989172591279')

# Умножение
c_new = (Decimal('2') * a ** Decimal('2')) ** Decimal('0.5')

# Вывод результата
print(c_new)
