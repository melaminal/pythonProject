import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

a = [3.887626363, 3.875030526, 3.867056867, 3.859193298, 3.851431120,
     3.843767485, 3.836151444, 3.828578693, 3.821056509, 3.813535902,
     3.806046760]
c = [7.778997835, 7.895682802, 7.973472780, 8.051262759, 8.129052737,
     8.206842715, 8.284632694, 8.362422672, 8.440212650, 8.518002629,
     8.595792607]

# Построение графика
plt.figure(figsize=(7, 5))
plt.plot(a, c, color='k', marker='s',
         markerfacecolor='k', markeredgecolor='k', markersize=6)

# Настройка графика
plt.xlabel("a", fontsize=14)
plt.ylabel(r"c", fontsize=14)
# plt.legend(frameon=False)

plt.minorticks_on()
plt.tick_params(which='both', direction='in', top=True, right=True, length=9, width=1, labelsize=12)
plt.tick_params(which='minor', length=4)

plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
plt.tight_layout()

ax = plt.gca()
ax.format_coord = lambda x, y: f"x = {x:.5f},   y = {y:.5f}"

plt.show()

