from decimal import Decimal, getcontext

# Установить точность до 17 знаков
getcontext().prec = 17

# global a, c
# a_glb =
# b_glb =
# c_glb =

# Определи числа
a = Decimal('3.8894989172591279')

# Умножение
c_new = a * Decimal('2')

# Вывод результата
print(c_new)
