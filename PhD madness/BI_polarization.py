import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

# Данные (# [ready] - можно анализировать CONTCARs и считать поляризацию)
# x_P4_mmm = [-5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
# y_P4_mmm = []

x_I4_mcm = [-6.5, -5.5, -4.5, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5]
y_I4_mcm = [0.0083, 0.0075, 0.0063, 0.0057, 0.0051, 0.0044, 0.0039, 0.0034, 0.0028, 0.0024] # P [µC cm⁻²] на 20-атомную ячейку, до вычета центросимметричной структуры

x_P4mm = [-8.00, -7.00, -6.00, -5.00, -4.00, -3.00]
y_P4mm = [8.4265, 10.6500, 14.5661, -6.5220, -13.6912, 7.4602]

# x_Imma = [-1.7, -1.2, -0.7, -0.2, 0.3, 0.8, 1.3, 1.8, 2.3, 2.8]
# y_Imma = []

# x_Pnma = [-1.8, -1.3, -0.8, -0.3, 0.2, 0.7, 1.2, 1.7, 2.2]
# y_Pnma = []

# x_C2_c = [-6.00, -5.00, -4.00, -3.00, -2.00, -1.00, 0.00, 1.00, 2.00, 3.00]
# y_C2_c = []

# x_C2_m = [-1.00, 0.00, 1.00, 2.00]
# y_C2_m = []

# x_Pmc2_1 = [2.00, 3.00, 4.00, 4.50, 5.00, 5.50, 6.00, 6.50, 7.00, 7.50, 8.00]
# y_Pmc2_1 = []

# x_I4cm = [-7.00, -6.00, -5.00, -4.00, -3.00, -2.00]
# y_I4cm = []

# x_Ima2 = [-2.9, -2.4, -1.9, -1.4, -0.9, -0.4, 0.1, 0.6, 1.1, 1.6]
# y_Ima2 = []

# x_P1_with_noise = [0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00]
# y_P1_with_noise = []

# Построение графиков
plt.figure(figsize=(6, 4))
plt.plot(x_I4_mcm, y_I4_mcm, color='k', marker='s', markerfacecolor='k',  markeredgecolor='k', markersize=6, label="I4/mcm")
plt.plot(x_P4mm, y_P4mm, color='#800080', markerfacecolor='#800080',  markeredgecolor='#800080', marker='o', label="P4mm")
# plt.plot(x_Imma, y_Imma, marker='D', color='lightseagreen', markerfacecolor='lightseagreen',  markeredgecolor='lightseagreen', label="Imma")
# plt.plot(x_Pnma, y_Pnma, color='#A52A2A', markerfacecolor='#A52A2A',  markeredgecolor='#A52A2A', marker='>', label="Pnma")
# plt.plot(x_C2_c, y_C2_c, marker='^', color='chartreuse', markerfacecolor='chartreuse',  markeredgecolor='chartreuse', label="C2/c")
# plt.plot(x_Pmc2_1, y_Pmc2_1, marker='H', color='olive', markerfacecolor='olive',  markeredgecolor='olive', label="Pmc2_1")
# plt.plot(x_I4cm , y_I4cm, color='m', markerfacecolor='m',  markeredgecolor='m', marker='<', label="I4cm")
# plt.plot(x_Ima2, y_Ima2, marker='v', color='b', markerfacecolor='b',  markeredgecolor='b', label="Ima2")
# plt.plot(x_P1_with_noise, y_P1_with_noise, marker='', color='', markerfacecolor='',  markeredgecolor='', label="P1_with_noise")

# Настройка графика
plt.title("Biaxial strain")
plt.xlabel("Misfit strain (%)", fontsize=14)
plt.ylabel("Polarization, mcC/cm-2", fontsize=14)
plt.tick_params(axis='both', direction='in', labelsize=12)
legend = plt.legend(frameon=False, loc='upper right', bbox_to_anchor=(0.9, 1.0))  # можно менять числа вручную


# Сохранение графика
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
plt.tight_layout()
plt.show()