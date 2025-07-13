import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

x_I4_mcm = [-6.5, -6.0, -5.5, -5.0, -4.5, -4.0, -3.5, -3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0,
            1.5, 2.5]
y_I4_mcm = [-199.18131787 / 4, -199.50326295 / 4, -199.78883877 / 4, -200.04258438 / 4, -200.26845997 / 4,
            -200.46588863 / 4, -200.62836649 / 4, -200.76875449 / 4, -200.87602930 / 4, -200.95960979 / 4,
            -201.01712198 / 4, -201.04793293 / 4, -201.05608183 / 4, -201.03925146 / 4, -200.99879285 / 4,
            -200.93779562 / 4, -200.84967770 / 4, -200.61369122 / 4]

x_P4mm = [-8.0, -7.0, -6.0, -5.0, -4.0]
y_P4mm = [-198.94392329 / 4, -199.28545880 / 4, -199.56498071 / 4, -199.80836376 / 4, -200.07911955 / 4]

x_Imma = [-1.7, -1.2, -0.7, -0.2, 0.3, 0.8, 1.3, 1.8, 2.3, 2.8, 3.2]
y_Imma = [-200.85609377 / 4, -200.94860524 / 4, -201.00902892 / 4, -201.03842772 / 4, -201.03859354 / 4,
          -201.01004625 / 4, -200.95436200 / 4, -200.87326401 / 4, -200.76673710 / 4, -200.63646444 / 4,
          -200.51563876 / 4]

x_Pnma = [-1.8, -1.3, -0.8, -0.3, 0.2, 0.7, 1.0, 1.2, 1.5, 1.7, 2.0, 2.2]
y_Pnma = [-200.87828623 / 4, -200.96077896 / 4, -201.01733471 / 4, -201.04766342 / 4, -201.05140161 / 4,
          -201.02760204 / 4, -200.99989912 / 4, -200.97620451 / 4, -200.93274590 / 4, -200.89925477 / 4,
          -200.84049693 / 4, -200.79660982 / 4]

x_C2_c = [-6.0, -5.5, -5.0, -4.5, -4.0, -3.5, -3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0,
          2.5, 3.0]
y_C2_c = []

x_Pmc2_1 = [5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0]
y_Pmc2_1 = [-199.80630681 / 4, -199.56316836 / 4, -199.30221605 / 4, -199.02500018 / 4, -198.73029503 / 4,
            -198.42078113 / 4, -198.09659195 / 4]

x_I4cm = [-7.0, -6.0, -5.0, -4.5, -4.0, -3.5, -3.0, -2.5, -2.0, -1.5]
y_I4cm = [-199.05897744 / 4, -199.58371107 / 4, -200.05978548 / 4, -200.27074406 / 4, -200.46284605 / 4,
          -200.62836312 / 4, -200.76591386 / 4, -200.87602653 / 4, -200.95961041 / 4, -201.01711920 / 4]

x_Ima2 = [-5.0, -4.5, -4.0, -3.5, -2.9, -2.4, -1.9, -1.6, -0.9, -0.4, 0.1, 0.6, 1.1, 1.6, 2.0, 3.0, 4.0,
          5.0, 6.0, 7.0]
y_Ima2 = [-200.04407958 / 4, -200.26845012 / 4, -200.46284277 / 4, -200.62836937 / 4, -200.79008887 / 4,
          -200.89487235 / 4, -200.97313467 / 4, -201.00758929 / 4, -201.05253736 / 4, -201.05579876 / 4,
          -201.03306095 / 4, -200.98796651 / 4, -200.92026898 / 4, -200.84611534 / 4, -200.78055575 / 4,
          -200.59459676 / 4, -200.38184223 / 4, -200.14698529 / 4, -199.89520407 / 4, -199.63215389 / 4]

# Построение графиков
plt.plot(x_I4_mcm, y_I4_mcm, color='k', linewidth=1.2, marker='s', markerfacecolor='k',  markeredgecolor='k', markersize=4, label="I4/mcm")
plt.plot(x_P4mm, y_P4mm, color='#800080', linewidth=1.2, markerfacecolor='#800080',  markeredgecolor='#800080', marker='o', markersize=4, label="P4mm")
plt.plot(x_Imma, y_Imma, marker='D', linewidth=1.2, color='lightseagreen', markerfacecolor='lightseagreen',  markeredgecolor='lightseagreen', markersize=4, label="Imma")
plt.plot(x_Pnma, y_Pnma, color='#A52A2A', linewidth=1.2, markerfacecolor='#A52A2A',  markeredgecolor='#A52A2A', marker='>', markersize=4, label="Pnma")
plt.plot(x_C2_c, y_C2_c, marker='^', linewidth=1.2, color='chartreuse', markerfacecolor='chartreuse',  markeredgecolor='chartreuse', markersize=4, label="C2/c")
plt.plot(x_Pmc2_1, y_Pmc2_1, marker='H', linewidth=1.2, color='olive', markerfacecolor='olive',  markeredgecolor='olive', markersize=4, label="Pmc2_1")
plt.plot(x_I4cm , y_I4cm, color='m', linewidth=1.2, markerfacecolor='m',  markeredgecolor='m', marker='<', markersize=4, label="I4cm")
plt.plot(x_Ima2, y_Ima2, marker='v', linewidth=1.2, color='b', markerfacecolor='b',  markeredgecolor='b', markersize=4, label="Ima2")

# Настройка графика
plt.xlabel("Biaxial strain, %", fontsize=14)
plt.ylabel("Energy per f.u., eV", fontsize=14)
plt.tick_params(axis='both', direction='in', size=7, labelsize=12)
legend = plt.legend(frameon=False, loc='upper right', bbox_to_anchor=(0.9, 1.0))  # можно менять числа вручную

plt.minorticks_on()
plt.tick_params(which='both', direction='in', top=True, right=True, length=9, width=1, labelsize=12)
plt.tick_params(which='minor', length=4)

# Сохранение графика
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
plt.tight_layout()
plt.show()