import matplotlib.pyplot as plt

# Данные
x_P4_mmm = [-5.00, -4.00, -3.00, -2.00, -1.00, 0.00, 1.00, 2.00, 3.00, 4.00, 5.00] # Фаза проверена
y_P4_mmm = [-199.154365510 / 4, -199.828844700 / 4, -200.325823990 / 4, -200.662947640 / 4, -200.855441340 / 4,
            -200.918217210 / 4, -200.863757400 / 4, -200.702980610 / 4, -200.445338970 / 4, -200.099874900 / 4,
            -199.674896790 / 4]

x_I4mcm = [-4.00, -3.00, -2.00, -1.00, 0.00, 0.50, 1.00, 2.00] # Фаза проверена
y_I4mcm = [-200.462847030 / 4, -200.765920710 / 4, -200.959607610 / 4, -201.049075670 / 4, -201.038515920 / 4,
           -200.999170270 / 4, -200.935652040 / 4, -200.742049550 / 4]

x_P4mm = [-8.00, -7.00, -6.00, -5.00, -4.00, -3.00] # Фаза проверена
y_P4mm = [-198.943953460 / 4, -199.285493010 / 4, -199.564980710 / 4, -199.808363760 / 4, -200.079119550 / 4,
          -200.403009200 / 4]

x_C2_m = [-1.00, 0.00, 1.00, 2.00, 3.00] # Фаза проверена
y_C2_m = [-201.049080990 / 4, -201.050489990 / 4, -200.992754040 / 4, -200.835519510 / 4, -200.579417690 / 4]

x_Pnma = [-1.00, 0.00, 1.00, 2.00, 3.00] # Фаза проверена
y_Pnma = [-200.997767250 / 4, -201.053085670 / 4, -200.999898660 / 4, -200.840539020 / 4, -200.582906320 / 4]

x_C2_c = [-1.00, 0.00, 1.00, 2.00, 3.00] # Фаза проверена
y_C2_c = [-201.049084340 / 4, -201.052852100 / 4, -200.999895620 / 4, -200.840498300 / 4, -200.582944320 / 4]

x_Pmc2_1 = [2.00, 3.00, 4.00, 5.00, 6.00, 7.00] # Фаза проверена
y_Pmc2_1 = [-200.863851580 / 4, -200.691550890 / 4, -200.487917020 / 4, -200.258320800 / 4, -200.007569500 / 4,
            -199.740011790 / 4]

x_I4cm = [-7.00, -6.00, -5.00, -4.00, -3.00, -2.00]
y_I4cm = []

x_Ima2 = [0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00]
y_Ima2 = [-201.038565010 / 4, -200.937097030 / 4, -200.784318220 / 4, -200.600821300 / 4, -200.390629910 / 4,
          -200.158382640 / 4, -199.909399670 / 4, -199.649103970 / 4]

# Построение графиков
plt.figure(figsize=(7, 6))

plt.plot(x_P4_mmm, y_P4_mmm, marker='o', label="P4/mmm")
plt.plot(x_I4mcm, y_I4mcm, marker='o', label="I4/mcm (a0a0c-)")
plt.plot(x_P4mm, y_P4mm, marker='o', label="P4mm")
plt.plot(x_Pnma, y_Pnma, marker='o', label="Pnma")
plt.plot(x_Pmc2_1, y_Pmc2_1, marker='o', label="Pmc2_1")
plt.plot(x_I4cm , y_I4cm, marker='o', label="I4cm")
plt.plot(x_Ima2, y_Ima2, marker='o', label="Ima2")
# Настройка графика
plt.title("Biaxial")
plt.xlabel("Biaxial strain (%)", fontsize=14)
plt.ylabel("Energy (eV)", fontsize=14)
plt.tick_params(axis='both', direction='in', labelsize=12)
plt.legend()
plt.grid(True)

# Показ графика
plt.show()
