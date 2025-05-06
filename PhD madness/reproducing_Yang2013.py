import matplotlib.pyplot as plt

# Данные (# [ready] - можно анализировать CONTCARs и считать поляризацию)
x_P4_mmm = [-5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0] # [ready]
y_P4_mmm = [-199.16470823 / 4, -199.83694117 / 4, -200.33169409 / 4, -200.66668161 / 4,
            -200.85727528 / 4, -200.91800767 / 4, -200.86165271 / 4, -200.69898904 / 4,
            -200.43956506 / 4, -200.09243430 / 4, -199.66572090 / 4]

x_I4_mcm = [-6.5, -5.5, -4.5, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5] # [ready]
y_I4_mcm = [-199.18131787 / 4, -199.78883877 / 4, -200.26845997 / 4, -200.62836649 / 4,
            -200.87602930 / 4, -201.01712198 / 4, -201.05608183 / 4, -200.99879285 / 4,
            -200.84967770 / 4, -200.61369122 / 4]

x_P4mm = [-8.00, -7.00, -6.00, -5.00, -4.00, -3.00] # [ready]
y_P4mm = [-198.94392329 / 4, -199.28545880 / 4, -199.56498071 / 4, -199.80836376 / 4,
          -200.07911955 / 4, -200.40300926 / 4]

x_Imma = [-1.7, -1.2, -0.7, -0.2, 0.3, 0.8, 1.3, 1.8, 2.3, 2.8] # [ready]
y_Imma = [-200.85609377 / 4, -200.94860524 / 4, -201.00902892 / 4, -201.03842772 / 4,
          -201.03859354 / 4, -201.01004625 / 4, -200.95436200 / 4, -200.87326401 / 4,
          -200.76673710 / 4, -200.63646444 / 4]

x_Pnma = [-1.8, -1.3, -0.8, -0.3, 0.2, 0.7, 1.2, 1.7, 2.2] # [ready]
y_Pnma = [-200.87828623 / 4, -200.96077896 / 4, -201.01733471 / 4, -201.04766342 / 4,
          -201.05140161 / 4, -201.02760204 / 4, -200.97620451 / 4, -200.89925477 / 4,
          -200.79660982 / 4]

x_C2_c = [-6.00, -5.00, -4.00, -3.00, -2.00, -1.00, 0.00, 1.00, 2.00, 3.00] # [ready]
y_C2_c = [-199.50159695 / 4, -200.04407379 / 4, -200.46282847 / 4, -200.76589262 / 4,
          -200.95959031 / 4, -201.04907864 / 4, -201.05284712 / 4, -200.99990060 / 4,
          -200.84049685 / 4, -200.58290141 / 4]

x_C2_m = [-1.00, 0.00, 1.00, 2.00] # [ready]
y_C2_m = [-201.04907433 / 4, -201.05048870 / 4, -200.99276861 / 4, -200.83551129 / 4]

x_Pmc2_1 = [2.00, 3.00, 4.00, 4.50, 5.00, 5.50, 6.00, 6.50, 7.00, 7.50, 8.00] # [ready]
y_Pmc2_1 = [-200.86385159 / 4, -200.69155089 / 4, -200.48792191 / 4, -200.37602462 / 4,
            -200.25832023 / 4, -200.13527809 / 4, -200.00756597 / 4, -199.87568663 / 4,
            -199.88278254 / 4, -199.82687388 / 4, -199.77477625 / 4]

x_I4cm = [-7.00, -6.00, -5.00, -4.00, -3.00, -2.00] # [ready]
y_I4cm = [-199.05897744 / 4, -199.58371107 / 4, -200.05978548 / 4, -200.46284605 / 4,
          -200.76591386 / 4, -200.95961041 / 4]

# x_Ima2 = [-2.9, -2.4, -1.9, -1.4, -0.9, -0.4, 0.1, 0.6, 1.1, 1.6]
# y_Ima2 = []

# x_P1_with_noise = [0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00]
# y_P1_with_noise = []

# Построение графиков
plt.figure(figsize=(7, 6))
plt.plot(x_I4_mcm, y_I4_mcm, color='k', marker='s', markerfacecolor='k',  markeredgecolor='k', markersize=6, label="I4/mcm")
plt.plot(x_P4mm, y_P4mm, color='#800080', markerfacecolor='#800080',  markeredgecolor='#800080', marker='o', label="P4mm")
plt.plot(x_Imma, y_Imma, marker='D', color='lightseagreen', markerfacecolor='lightseagreen',  markeredgecolor='lightseagreen', label="Imma")
plt.plot(x_Pnma, y_Pnma, color='#A52A2A', markerfacecolor='#A52A2A',  markeredgecolor='#A52A2A', marker='>', label="Pnma")
plt.plot(x_C2_c, y_C2_c, marker='^', color='chartreuse', markerfacecolor='chartreuse',  markeredgecolor='chartreuse', label="C2/c")
plt.plot(x_Pmc2_1, y_Pmc2_1, marker='H', color='olive', markerfacecolor='olive',  markeredgecolor='olive', label="Pmc2_1")
plt.plot(x_I4cm , y_I4cm, color='m', markerfacecolor='m',  markeredgecolor='m', marker='<', label="I4cm")
# plt.plot(x_Ima2, y_Ima2, marker='v', color='b', markerfacecolor='b',  markeredgecolor='b', label="Ima2")
# plt.plot(x_P1_with_noise, y_P1_with_noise, marker='', color='', markerfacecolor='',  markeredgecolor='', label="P1_with_noise")

# Настройка графика
plt.title("Biaxial strain")
plt.xlabel("Misfit strain (%)", fontsize=14)
plt.ylabel("Energy (eV)", fontsize=14)
plt.tick_params(axis='both', direction='in', labelsize=12)
plt.legend()
plt.grid(True)

# Сохранение графика
plt.show()
# plt.savefig("my_plot.png")