import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

uni_strain = [0.0, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]
polarization = [0.0000, -0.1262, -0.2465, -0.3343, -0.4067, -0.4697, -0.5260,
 -0.5770, -0.6233, -0.6664, -0.7064]

# Построение графика
plt.figure(figsize=(7, 5))
plt.plot(uni_strain, polarization, color='k', marker='s',
         markerfacecolor='k', markeredgecolor='k', markersize=6)

# Настройка графика
plt.xlabel("Misfit strain, %", fontsize=14)
plt.ylabel(r"Polarization, C/m$^2$", fontsize=14)
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# plt.legend(frameon=False)

plt.minorticks_on()
plt.tick_params(which='both', direction='in', top=True, right=True, length=9, width=1, labelsize=12)
plt.tick_params(which='minor', length=4)

plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
plt.tight_layout()
plt.show()

