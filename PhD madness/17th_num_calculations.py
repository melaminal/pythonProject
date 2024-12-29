from decimal import Decimal, getcontext

# Установить точность до 17 знаков
getcontext().prec = 17

# for FM state global a, c
# a_glb = 3.9394478321811017
# b_glb = -3.9394478321811017
# c_glb = 7.8788956643622034

# Определи числа
a = Decimal('3.8896580000380268')

# Умножение
c = a * Decimal('2')

# Вывод результата
print(c)
