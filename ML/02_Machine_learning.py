# Код для простейшего перцептрона на примере классификации образов в 2 класса (Френк Розенблатт, 1957 год):
# разделяющая прямая / разделяющая гиперплоскость
# (https://www.youtube.com/watch?v=t9QfcFNkG58&list=PLA0M1Bcd0w8yv0XGiF1wjerjSZVSrYbjh&index=3)

import numpy as np
import matplotlib.pyplot as plt

N = 5 # по 5 образов для обоих классов

# точки х1 и х2 лежат выше прямой
x1 = np.random.random(N) # случайные величины по одной оси
x2 = x1 + [np.random.randint(10)/10 for i in range(N)] # -//- + случайные отклонения
C1 = [x1, x2]

# точки х1 и х2 лежат ниже прямой
x2 = np.random.random(N)
x2 = x1 - [np.random.randint(10)/10 for i in range(N)] - 0.1
C2 = [x1, x2]

f = [0, 1]

# коэффициент угла наклона k = -tg(a) = -w1/w2 (веса)
W = np.array([-0.3, 0.3]) # весовые коэффициенты (если поставить неравные, то классы будут определены неверно!!!)
for i in range(N):
    x = np.array([C2[0][i], C2[1][i]])
    y = np.dot(W, x)
    if y >= 0:
        print("Класс С1")
    else:
        print("Класс С2")

plt.scatter(C1[0][:], C1[1][:], s=10, c='red')
plt.scatter(C2[0][:], C2[1][:], s=10, c='blue')
plt.plot(f)
plt.grid(True)
plt.show()
