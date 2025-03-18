import matplotlib.pyplot as plt

# Данные
x_P4_mmm = [0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00] # Фаза проверена
y_P4_mmm = []

x_I4_mcm = [0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00] # Фаза проверена
y_I4_mcm = []

x_P4_mbm = [0.00, 1.00, 2.00, 3.00, 4.00, 7.00, 8.00, 9.00, 10.00] # Фаза проверена
y_P4_mbm = []

x_C2_m = [0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00]
y_C2_m = []

x_Cmcm = [0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00]
y_Cmcm = []

x_Pnma = [0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00]
y_Pnma = []

x_R_3c = [0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00]
y_R_3c = []

x_P4mm = [0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00]
y_P4mm = []

x_P1 = [0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00]
y_P1 = []

# x_Imma = [0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00]
# y_Imma = []

# x_C2_c = [0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00]
# y_C2_c = []

# x_Pmc2_1 = [0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00]
# y_Pmc2_1 = []

# x_I4cm = [0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00]
# y_I4cm = []

# x_Ima2 = [0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00]
# y_Ima2 = []

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
