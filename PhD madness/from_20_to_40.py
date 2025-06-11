#!/usr/bin/env python3
import numpy as np
from pathlib import Path

# ---------- 1. Чтение POSCAR ----------
with open("POSCAR", "r") as f:
    lines = f.readlines()

title = lines[0].strip()
scale = float(lines[1].strip())

# Векторы решётки (строки 3–5) с учётом масштаба
lattice_old = np.array([list(map(float, lines[i].split()))
                        for i in (2, 3, 4)]) * scale

# Параметры старой ячейки
a = lattice_old[0][0]            # компонент a-вектора вдоль x
c = lattice_old[2][2]
b = 2 * a                        # новое ортогональное ребро

# Новый ортогональный базис
lattice_new = np.array([[b, 0, 0],
                        [0, b, 0],
                        [0, 0, c]])

# ---------- 2. Считывание дробных координат ----------
coords_frac = np.array([list(map(float, line.split()))
                        for line in lines[8:28]])   # 20 атомов

# ---------- 3. Дробные → картезианские (покомпонентно) ----------
cart_coords = coords_frac * np.array([a * np.sqrt(2), a * np.sqrt(2), c])

# Поворот на –45° вокруг z
theta  = -np.pi/4
rot_z  = np.array([[np.cos(theta), -np.sin(theta), 0],
                   [np.sin(theta),  np.cos(theta), 0],
                   [0,              0,            1]])
cart_rot = cart_coords @ rot_z.T

# Картезианские → новые дробные
coords_new = cart_rot / np.array([b, b, c])
coords_new = coords_new % 1.0          # привести в диапазон [0,1)

# ---------- 4. Разбиваем на Eu / Ti / O ----------
eu  = coords_new[:4]          # первые 4 строки
ti  = coords_new[4:8]         # 5-8 строки
oxy = coords_new[8:]          # остальные 12

# ---------- 5. Создаём новые атомы ----------
# 4 Eu – прибавляем +0.5 к координате y
eu_extra = eu.copy()
eu_extra[:, 1] += 0.5            # y_old → y_old + 0.5
eu_extra %= 1.0                  # на случай выхода за пределы 1

# 4 Ti – тем, у кого x≈0.25, прибавляем +0.5 (0.25 → 0.75)
ti_extra = ti.copy()
tol = 1e-6
mask = np.abs(ti_extra[:, 0] - 0.25) < tol
ti_extra[mask, 0] += 0.5
ti_extra %= 1.0                  # нормализуем в [0,1)

# копии O1–O4 и O9–O12  (индексы 0–3 и 8–11)  → +0.5 по x
idx_x = [0, 1, 2, 3, 8, 9, 10, 11]
o_extra_x = oxy[idx_x].copy()
o_extra_x[:, 0] += 0.5
o_extra_x %= 1.0

# копии O5–O8  (индексы 4–7)  → +0.5 по y
idx_y = [4, 5, 6, 7]
o_extra_y = oxy[idx_y].copy()
o_extra_y[:, 1] += 0.5
o_extra_y %= 1.0

# ---------- 5. Собираем итоговый массив ----------
coords_final = np.vstack([eu, eu_extra, ti, ti_extra, oxy, o_extra_x, o_extra_y])  # (28,3)

# ---------- 6. Записываем новый POSCAR ----------
with open("POSCAR_28atoms", "w") as fout:
    fout.write(f"{title}_28atoms\n")
    fout.write("1.0\n")
    for v in lattice_new:
        fout.write(f"  {v[0]:.16f}  {v[1]:.16f}  {v[2]:.16f}\n")
    fout.write("Eu Ti O\n")
    fout.write("8 8 24\n")            # обновлённый счётчик
    fout.write("Direct\n")
    for xyz in coords_final:
        fout.write(f"  {xyz[0]:.16f}  {xyz[1]:.16f}  {xyz[2]:.16f}\n")

print("Готово: POSCAR_28atoms создан (8 Eu, 8 Ti, 12 O).")
