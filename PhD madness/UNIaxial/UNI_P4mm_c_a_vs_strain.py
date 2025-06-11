import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

uni_strain = [0.0, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]
c_a = [1.0004817, 1.0187898, 1.0309485, 1.0431277, 1.0553288, 1.0675519,
       1.0798104, 1.0921054, 1.1044344, 1.1168116, 1.1292285]

# Построение графика
plt.figure(figsize=(7, 5))
plt.plot(uni_strain, c_a, color='k', marker='s',
         markerfacecolor='k', markeredgecolor='k', markersize=6)

# Настройка графика
plt.xlabel("Misfit strain, %", fontsize=14)
plt.ylabel(r"c/a", fontsize=14)
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# plt.legend(frameon=False)

plt.minorticks_on()
plt.tick_params(which='both', direction='in', top=True, right=True, length=9, width=1, labelsize=12)
plt.tick_params(which='minor', length=4)

plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
plt.tight_layout()
plt.show()

