import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Данные вручную переписаны из изображения
data = {
    "strain": [-8.0, -7.0, -6.0, -5.0, -4.0, -3.0, 0.0],  # Примерные значения, замени на реальные
    "ionic_x": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ...],
    "electronic_x": [0.00002, -3.61723, -0.00001, -0.00004, 3.73384, 3.77277, ...],
    "ionic_y": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ...],
    "electronic_y": [7.15671, -3.61718, 0.00006, 0.00008, -3.73385, 3.77287, ...],
    "ionic_z": [69.21524, 65.19038, 59.54596, 50.15871, 32.84904, 21.01872, ...],
    "electronic_z": [5.77768, 8.53238, -5.88794, 2.68740, 3.02402, 0.28875, ...],
}

df = pd.DataFrame(data)

# Вычтем целые кратные дипольного кванта для пустых точек
quantum = 10  # Условное значение, подбери по графику
offsets = [-quantum, 0, quantum]

# Функция для отображения графиков
def plot_dipole_moments(df):
    directions = ['x', 'y', 'z']
    fig, axs = plt.subplots(2, 3, figsize=(12, 8))
    for i, dir in enumerate(directions):
        # Верхняя строка — электронный вклад
        ax = axs[0, i]
        ax.set_title(f"Along {dir}")
        ax.set_xlabel("Biaxial Strain (%)")
        ax.set_ylabel("Electronic dip. mom. (eÅ)")
        ax.plot(df["strain"], df[f"electronic_{dir}"], 'o', color='purple', label="electronic")
        for offset in offsets:
            if offset != 0:
                ax.plot(df["strain"], df[f"electronic_{dir}"] + offset, 'o', mfc='white', mec='purple')
        ax.axhline(0, color='black', linewidth=0.5)

        # Нижняя строка — ионный вклад
        ax = axs[1, i]
        ax.set_xlabel("Biaxial Strain (%)")
        ax.set_ylabel("Ionic dip. mom. (eÅ)")
        ax.plot(df["strain"], df[f"ionic_{dir}"], 'o', color='purple', label="ionic")
        for offset in offsets:
            if offset != 0:
                ax.plot(df["strain"], df[f"ionic_{dir}"] + offset, 'o', mfc='white', mec='purple')
        ax.axhline(0, color='black', linewidth=0.5)

    plt.tight_layout()
    plt.show()

plot_dipole_moments(df)
