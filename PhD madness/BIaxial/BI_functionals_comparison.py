import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

# Данные
x_I4_mcm_PBEsol = [-6.5, -5.5, -4.5, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5]
y_I4_mcm_PBEsol = [-199.18131787 / 4, -199.78883877 / 4, -200.26845997 / 4, -200.62836649 / 4,
                   -200.87602930 / 4, -201.01712198 / 4, -201.05608183 / 4, -200.99879285 / 4,
                   -200.84967770 / 4, -200.61369122 / 4]

x_I4_mcm_PBE = [-6.5, -5.5, -4.5, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5]
y_I4_mcm_PBE = [-190.42489124 / 4, -191.16274376 / 4, -191.77045493 / 4, -192.25842321 / 4,
                -192.63411111 / 4, -192.90436080 / 4, -193.07422411 / 4, -193.14908813 / 4,
                -193.13150711 / 4, -193.02859350 / 4]

x_Pnma_PBEsol = [-1.8, -1.3, -0.8, -0.3, 0.2, 0.7, 1.2, 1.7, 2.2]
y_Pnma_PBEsol = [-200.87828623 / 4, -200.96077896 / 4, -201.01733471 / 4, -201.04766342 / 4,
                 -201.05140161 / 4, -201.02760204 / 4, -200.97620451 / 4, -200.89925477 / 4,
                 -200.79660982 / 4]

x_Pnma_PBE = [-1.8, -1.3, -0.8, -0.3, 0.2, 0.7, 1.2, 1.7, 2.2]
y_Pnma_PBE = [-192.68819821 / 4, -192.82161757 / 4, -192.92604104 / 4, -193.02468734 / 4,
              -193.09153171 / 4, -193.13439273 / 4, -193.15217887 / 4, -193.14374003 / 4,
              -193.10979210 / 4]

# Построение графиков
plt.figure(figsize=(5, 5))
plt.plot(x_I4_mcm_PBEsol, y_I4_mcm_PBEsol, color='k', marker='s', markerfacecolor='k',  markeredgecolor='k', markersize=6, label="I4/mcm_PBEsol+U")
plt.plot(x_I4_mcm_PBE, y_I4_mcm_PBE, marker='^', color='chartreuse', markerfacecolor='chartreuse',  markeredgecolor='chartreuse', label="I4/mcm_PBE+U")
plt.plot(x_Pnma_PBEsol, y_Pnma_PBEsol, color='r', marker='s', markerfacecolor='r',  markeredgecolor='r', markersize=6, label="Pnma_PBEsol+U")
plt.plot(x_Pnma_PBE, y_Pnma_PBE, marker='^', color='b', markerfacecolor='b',  markeredgecolor='b', label="Pnma_PBE+U")

# Настройка графика
plt.xlabel("Biaxial strain, %", fontsize=14)
plt.ylabel("Energy per f.u., eV", fontsize=14)
plt.tick_params(axis='both', direction='in', size=7, labelsize=12)
plt.xticks([-6, -4, -2, 0, 2])
plt.legend(frameon=False)

plt.minorticks_on()
plt.tick_params(which='both', direction='in', top=True, right=True, length=9, width=1, labelsize=12)
plt.tick_params(which='minor', length=4)

# Сохранение графика
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
plt.tight_layout()
plt.show()

