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

# x_I4_mcm_HSE06 = [-6.5, -5.5, -4.5, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5]
# x_I4_mcm_HSE06 = []

# Построение графиков
plt.figure(figsize=(3, 5))
plt.plot(x_I4_mcm_PBEsol, y_I4_mcm_PBEsol, color='k', marker='s', markerfacecolor='k',  markeredgecolor='k', markersize=6, label="PBEsol+U")
plt.plot(x_I4_mcm_PBE, y_I4_mcm_PBE, marker='^', color='chartreuse', markerfacecolor='chartreuse',  markeredgecolor='chartreuse', label="PBE+U")
# plt.plot(x_I4_mcm_HSE06, x_I4_mcm_HSE06, color='#800080', markerfacecolor='#800080',  markeredgecolor='#800080', marker='o', label="HSE06+U")

# Настройка графика
plt.xlabel("Misfit strain, %", fontsize=14)
plt.ylabel("Energy per f.u., eV", fontsize=14)
plt.tick_params(axis='both', direction='in', size=7, labelsize=12)
plt.xticks([-6, -4, -2, 0, 2])
plt.legend(frameon=False)

# Сохранение графика
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
plt.tight_layout()
plt.show()

