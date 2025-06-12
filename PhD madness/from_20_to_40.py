#!/usr/bin/env python3
import numpy as np
from pathlib import Path

# ---------- 1. Чтение POSCAR ----------
with open("POSCAR_P4mm", "r") as f:
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

# ---------- 6. Создаём новые атомы O ----------
ti_all_frac = np.vstack([ti, ti_extra])     # 8 Ti (4 + 4)
ti_all_cart = ti_all_frac @ lattice_new     # картезианские Ti

o_extra = []

# --- группы индексов ---
idx_reflect = list(range(8))                # O1–O8 → зеркалим через Ti
idx_plane_x = [8, 9, 10, 11]                # O9–O12 → отражение x→x+0.5

for i, o_frac in enumerate(oxy):
    o_cart = o_frac @ lattice_new

    if i in idx_reflect:
        # ---- зеркалирование через ближайший Ti ----
        j_min = np.argmin(np.linalg.norm(ti_all_cart - o_cart, axis=1))
        ti_cart = ti_all_cart[j_min]
        o_copy_cart = 2.0 * ti_cart - o_cart
        o_copy_frac = (o_copy_cart @ np.linalg.inv(lattice_new)) % 1.0

        # если случайно получили ту же точку — fallback ±0.5 по y
        if np.allclose(o_copy_frac, o_frac, atol=1e-6):
            o_copy_frac[1] = (o_copy_frac[1] + 0.5) % 1.0

        o_extra.append(o_copy_frac)

    elif i in idx_plane_x:
        # ---- отражение через плоскость x = 0.5 ----
        o_copy_frac = o_frac.copy()
        o_copy_frac[0] = (o_copy_frac[0] + 0.5) % 1.0
        o_extra.append(o_copy_frac)

o_extra = np.array(o_extra)                 # 12 новых O-копий

# ---------- 5. Собираем итоговый массив ----------
coords_final = np.vstack([eu, eu_extra, ti, ti_extra, oxy, o_extra])  # (28,3)

# ---------- 6. Записываем новый POSCAR ----------
with open("POSCAR_40atoms", "w") as fout:
    fout.write(f"{title}_40atoms\n")
    fout.write("1.0\n")
    for v in lattice_new:
        fout.write(f"  {v[0]:.16f}  {v[1]:.16f}  {v[2]:.16f}\n")
    fout.write("Eu Ti O\n")
    fout.write("8 8 24\n")            # обновлённый счётчик
    fout.write("Direct\n")
    for xyz in coords_final:
        fout.write(f"  {xyz[0]:.16f}  {xyz[1]:.16f}  {xyz[2]:.16f}\n")

print("Готово: POSCAR_40atoms создан (8 Eu, 8 Ti, 24 O).")
