import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

# Данные
strain = [0.0, 1.2, 2.2, 3.2, 4.2, 5.2, 6.2, 8.2, 9.2, 10.2]
angle = [8.0215563, 8.6212164, 9.0837579, 9.5097122, 9.9075980, 10.2789369,
         10.6241209, 11.2455581, 11.5208707, 11.7773889]


# Построение графика
plt.figure(figsize=(7, 5))
plt.plot(strain, angle, color='k', marker='s',
         markerfacecolor='k', markeredgecolor='k', markersize=6)

# Настройка графика
plt.xlabel("Misfit strain, %", fontsize=14)
plt.ylabel("Angle, °", fontsize=14)
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
plt.legend(frameon=False)

plt.minorticks_on()
plt.tick_params(which='both', direction='in', top=True, right=True, length=9, width=1, labelsize=12)
plt.tick_params(which='minor', length=4)

plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
plt.tight_layout()
plt.show()
