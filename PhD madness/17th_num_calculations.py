from decimal import Decimal, getcontext

from mpmath import sqrtm

# Установить точность до 17 знаков
getcontext().prec = 17

# global a, c
# a_glb = 3.8894989172591279
# b_glb = -3.8894989172591279
# c_glb = 7.7789978345182558

# Определи числа
a = Decimal('7.7789978345182558')

# Умножение
c_new = a * Decimal('1.05')

# Вывод результата
print(c_new)
