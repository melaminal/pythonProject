import matplotlib.pyplot as plt

# Данные
x_I4_mcm = [-4.00, -3.00, -2.00, -1.00, 0.00, 0.50, 1.00, 2.00] # Фаза проверена
y_I4_mcm = [-200.462847030 / 4, -200.765920710 / 4, -200.959607610 / 4, -201.049075670 / 4, -201.038515920 / 4,
           -200.999170270 / 4, -200.935652040 / 4, -200.742049550 / 4]

x_P4mm = [-8.00, -7.00, -6.00, -5.00, -4.00, -3.00] # Фаза проверена
y_P4mm = [-198.943953460 / 4, -199.285493010 / 4, -199.564980710 / 4, -199.808363760 / 4, -200.079119550 / 4,
          -200.403009200 / 4]

x_Imma = [-2.00, -1.00, 0.00, 2.00, 3.00]
y_Imma = [-200.784417960 / 4, -200.976536170 / 4, -201.041885890 / 4, -200.833491890 / 4, -200.577820510 / 4]

x_Pnma = [-1.00, 0.00, 1.00, 2.00, 3.00] # Фаза проверена
y_Pnma = [-200.997767250 / 4, -201.053085670 / 4, -200.999898660 / 4, -200.840539020 / 4, -200.582906320 / 4]

x_C2_c = [-1.00, 0.00, 1.00, 2.00, 3.00] # Фаза проверена
y_C2_c = [-201.049084340 / 4, -201.052852100 / 4, -200.999895620 / 4, -200.840498300 / 4, -200.582944320 / 4]

x_Pmc2_1 = [2.00, 3.00, 4.00, 5.00, 6.00, 7.00] # Фаза проверена
y_Pmc2_1 = [-200.863851580 / 4, -200.691550890 / 4, -200.487917020 / 4, -200.258320800 / 4, -200.007569500 / 4,
            -199.740011790 / 4]

x_I4cm = [-7.00, -6.00, -5.00, -4.00, -3.00, -2.00] # Фаза проверена
y_I4cm = [-199.058979720 / 4, -199.583121550 / 4, -200.059696990 / 4, -200.462840000 / 4, -200.76591399 / 4,
          -200.959610370 / 4]

x_Ima2 = [0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00] # Фаза проверена
y_Ima2 = [-201.039256210 / 4, -200.936202140 / 4, -200.780555550 / 4, -200.594596760 / 4, -200.381842180 / 4,
          -200.146985260 / 4, -199.895204080 / 4, -199.632142410 / 4]

# Построение графиков
plt.figure(figsize=(7, 6))
plt.plot(x_I4_mcm, y_I4_mcm, color='k', marker='s', markerfacecolor='k',  markeredgecolor='k', markersize=6, label="I4/mcm")
plt.plot(x_P4mm, y_P4mm, color='#800080', markerfacecolor='#800080',  markeredgecolor='#800080', marker='o', label="P4mm")
plt.plot(x_Imma, y_Imma, marker='D', color='lightseagreen', markerfacecolor='lightseagreen',  markeredgecolor='lightseagreen', label="Imma")
plt.plot(x_Pnma, y_Pnma, color='#A52A2A', markerfacecolor='#A52A2A',  markeredgecolor='#A52A2A', marker='>', label="Pnma")
plt.plot(x_C2_c, y_C2_c, marker='^', color='chartreuse', markerfacecolor='chartreuse',  markeredgecolor='chartreuse', label="C2/c")
plt.plot(x_Pmc2_1, y_Pmc2_1, marker='H', color='olive', markerfacecolor='olive',  markeredgecolor='olive', label="Pmc2_1")
plt.plot(x_I4cm , y_I4cm, color='m', markerfacecolor='m',  markeredgecolor='m', marker='<', label="I4cm")
plt.plot(x_Ima2, y_Ima2, marker='v', color='b', markerfacecolor='b',  markeredgecolor='b', label="Ima2")
# Настройка графика
plt.title("Biaxial strain")
plt.xlabel("Misfit strain (%)", fontsize=14)
plt.ylabel("Energy (eV)", fontsize=14)
plt.tick_params(axis='both', direction='in', labelsize=12)
plt.legend()

# Сохранение графика
# plt.show()
plt.savefig("my_plot.png")
