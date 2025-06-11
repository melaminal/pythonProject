import numpy as np
from pathlib import Path

# ---------- 1. Чтение POSCAR ----------
with open("POSCAR", "r") as f:
    lines = f.readlines()

title = lines[0].strip()
scale = float(lines[1].strip())

# Векторы решетки (строки 3–5)
lattice_old = np.array([
    list(map(float, lines[2].split())),
    list(map(float, lines[3].split())),
    list(map(float, lines[4].split()))
]) * scale  # масштабируем

# Вычисляем параметры новой решетки
a = np.linalg.norm(lattice_old[0])
b = np.sqrt(2) * a
c = lattice_old[2][2]

# Новый ортогональный базис
lattice_new = np.array([
    [b, 0.0, 0.0],
    [0.0, b, 0.0],
    [0.0, 0.0, c]
])

# ---------- 2. Считывание координат атомов ----------
coords_frac = np.array([
    list(map(float, line.split()))
    for line in lines[8:28]  # строки 9–28, индексы 8–27
])

# ---------- 3. Поворот координат ----------
# дробные → картезианские
cart_coords = coords_frac @ lattice_old

# Поворот на –45° вокруг z
theta = -np.pi / 4
rot_z = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta),  np.cos(theta), 0],
    [0,              0,             1]
])
cart_rot = cart_coords @ rot_z.T

# Картезианские → новые дробные
coords_new = cart_rot @ np.linalg.inv(lattice_new)
coords_new = coords_new % 1.0  # приведение в [0, 1)

# ---------- 4. Вывод POSCAR ----------
with open("POSCAR_rotated", "w") as f_out:
    f_out.write(f"{title}_rotated\n")
    f_out.write("1.0\n")
    for vec in lattice_new:
        f_out.write("  {:.16f}  {:.16f}  {:.16f}\n".format(*vec))
    f_out.writelines(lines[5:7])  # названия атомов и их количества
    f_out.write("Direct\n")
    for row in coords_new:
        f_out.write("  {:.16f}  {:.16f}  {:.16f}\n".format(*row))

print("Готово: POSCAR_rotated создан.")
