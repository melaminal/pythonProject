from decimal import Decimal, getcontext

# Установить точность до 17 знаков
getcontext().prec = 17

# Определи числа
a = Decimal('3.86115895456069591')

# Умножение
c = a * 2

# Вывод результата
print(c)