import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

# Данные
strain = [0.0, 1.2, 2.2, 3.2, 4.2, 5.2, 8.2, 9.2, 10.2]
energy = [(-201.04667754 - (-201.04667754))/4,
          (-201.05141129 - (-201.04667754))/4,
          (-201.01280646 - (-201.04667754))/4,
          (-200.93919051 - (-201.04667754))/4,
          (-200.83422729 - (-201.04667754))/4,
          (-200.70125883 - (-201.04667754))/4,
          (-200.15780939 - (-201.04667754))/4,
          (-199.93638701 - (-201.04667754))/4,
          (-199.69858416 - (-201.04667754))/4]

# Построение графика
plt.figure(figsize=(7, 5))
plt.plot(strain, energy, color='k', marker='s',
         markerfacecolor='k', markeredgecolor='k', markersize=6)

# Настройка графика
plt.xlabel("Misfit strain, %", fontsize=14)
plt.ylabel(r"$E_{\mathrm{strained}} - E_{0\%\,\mathrm{strain}}$ per f.u., eV", fontsize=14)
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
plt.legend(frameon=False)

plt.minorticks_on()
plt.tick_params(which='both', direction='in', top=True, right=True, length=9, width=1, labelsize=12)
plt.tick_params(which='minor', length=4)

plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
plt.tight_layout()
plt.show()
