import matplotlib.pyplot as plt

# Данные
x_I4_mcm = [-6.5, -5.5, -4.5, -3.5, -2.5, -1.5, 0.5, 1.5, 2.5] # Фаза проверена
y_I4_mcm = [-199.18131010 / 4, -199.78884045 / 4, -200.26845200 / 4, -200.62837105 / 4, -200.87602913 / 4,
            -201.01712175 / 4, -200.99879278 / 4, -200.84967545 / 4, -200.61368701 / 4]

x_P4mm = [-8.00, -7.00, -6.00, -5.00, -4.00, -3.00] # Фаза проверена
y_P4mm = [-198.943953460 / 4, -199.285493010 / 4, -199.564980710 / 4, -199.808363760 / 4, -200.079119550 / 4,
          -200.403009200 / 4]

x_Imma = [-1.7, -1.2, -0.7, -0.2, 0.3, 0.8, 1.3, 1.8, 2.3, 2.8]
y_Imma = [-200.85609377 / 4, -200.94859500 / 4, -201.00902886 / 4, -201.03841397 / 4, -201.03859354 / 4,
          -201.01004582 / 4, -200.95435872 / 4, -200.87326376 / 4, -200.76672965 / 4, -200.63645668 / 4]

x_Pnma = [-1.8, -1.3, -0.8, -0.3, 0.2, 0.7, 1.2, 1.7, 2.2] # Фаза проверена
y_Pnma = [-200.87831292 / 4, -200.96077869 / 4, -201.01733454 / 4, -201.04765508 / 4, -201.05140027 / 4,
          -201.02760208 / 4, -200.97619877 / 4, -200.89926847 / 4, -200.79660995 / 4]

x_C2_c = [-6.00, -5.00, -4.00, -3.00, -2.00, -1.00, 0.00, 1.00, 2.00, 3.00] # Фаза проверена
y_C2_c = [-199.50159099 / 4, -200.04406508 / 4, -200.46284892 / 4, -200.76591884 / 4, -200.95959861 / 4,
          -201.049084340 / 4, -201.052852100 / 4, -200.999895620 / 4, -200.840498300 / 4, -200.582944320 / 4]

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
